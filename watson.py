import base64
import config
import httplib
import json
import logging
import utils

from datetime import datetime
from google.appengine.api import urlfetch
from models.question import Question
from models.business import Business
from models.stats import Stats
from utils import authenticate
from watson_exceptions import ConfigurationError, WatsonError


class AskWatson(utils.Handler):
    '''Given a question, query Watson for the answer.'''

    # Returns the entire json response
    @authenticate
    def get(self):
        conf = config.CONFIG_DB

        # Verify the instance is configured.
        conf_defaults = config.CONFIG_DEFAULTS
        if (conf.username == conf_defaults['DEFAULT_USERNAME']
                or conf.password == conf_defaults['DEFAULT_PASSWORD']
                or conf.watson_url == conf_defaults['DEFAULT_WATSON_URL']):

            raise ConfigurationError('Open the admin console and edit the '
                                     'config master entry to include your '
                                     'username and password')

        # Fetch singe-pass answers (ask Watson the question as given)
        
        # Load question from request, with a given default.
        question = self.request.get('q', 'Where can I find food for my pet?')
        sp_payload = {
            'question': {
                'questionText': question
            }
        }
        logging.info('Asking Watson: "{q}"'.format(q=question))
        sp_answers = self.query_watson(conf, sp_payload)

        full_answer = self.request.get('sf')
        if full_answer:
            self.render_json(json.dumps(sp_answers))
            return
        
        # Double-pass query. 
        # TODO(jabrouwer82): Fix the payload and change the conditional.
        # First query Watson restricted to our question doc
        # Use the title of that answer as the question for the second query
        # This payload does not work, but will be left in for future debugging. 
        dp_p1_payload = {
            'question': {
                'questionText': question,
                'filters': [{
                    'filterType': 'metadataFilter',
                    'fieldName': 'indexedKey.originalfile',
                    'values': [
                        'meta-question-doc.html'
                    ]
                }]
            }
        }
        logging.info('Asking Watson: "{q}"'.format(q=question))
        dp_p1_answers = self.query_watson(conf, sp_payload)
        full_answer = self.request.get('d1f')
        if full_answer:
            self.render_json(json.dumps(dp_p1_answers))
            return
        
        dp_p2_answers = dp_p1_answers
        # TODO(jabrouwer82): This isn't how this should be done, fix it.
        if dp_p1_answers['question']['evidencelist'][0]['metadataMap']['originalfile'] == 'meta-question-doc.html':
            dp_p2_question = dp_p1_answers['question']['answers'][0]['text'].split(' : ')[1]
            sp_payload['question']['questionText'] = dp_p2_question
            dp_p2_answers = self.query_watson(conf, sp_payload)
            full_answer = self.request.get('d2f')
            if full_answer:
                self.render_json(json.dumps(dp_p2_answers))
                return
        
        answers = self.merge_answers(sp_answers, dp_p2_answers)
        
        log = self.request.get('l')
        if log:
            self.log(question, answers)
        
        self.render_json(json.dumps(answers))

    def merge_answers(self, first, second):
        # TODO(jabrouwer82): Implement an option to return merged, unformatted answers
        answers = {}
        answers['answers'] = []
        first_index = 0
        second_index = 0
        for x in xrange(5):
            first_answer = first['question']['answers'][first_index]
            second_answer = second['question']['answers'][second_index]
            
            if first_answer['confidence'] > second_answer['confidence']:
                answer = first_answer
                document = first['question']['evidencelist'][first_index]['metadataMap']['title']
                first_index += 1
                single_pass = True
            else:
                answer = second_answer
                document = second['question']['evidencelist'][second_index]['metadataMap']['title']
                second_index += 1
                single_pass = False

            service_name = document.split(' : ')[1]
            services = Business.query(Business.name == service_name).fetch()
            service = services[0].to_dict() if len(services) > 0 else []
            response = {'answer': answer,
                        'service': service,
                        'id': x,
                        'single_pass_answer': single_pass
                       }
            answers['answers'].append(response)
        return answers



    def query_watson(self, conf, payload):
        # Standard HTTP basic authorization, base 64 encode username:password
        auth = 'Basic ' + base64.b64encode(
               '{username}:{password}'.format(
                   username=conf.username,
                   password=conf.password))

        headers = {
            'Authorization': auth,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-SyncTimeout': 30
        }

        # 60 seconds is the maximum time allowed on urlfetch for HTTP requests.
        urlfetch.set_default_fetch_deadline(60)
        r = urlfetch.fetch(url=conf.watson_url,
                           payload=json.dumps(payload),
                           method=urlfetch.POST,
                           headers=headers)

        if r.status_code == httplib.OK:
            answers = json.loads(r.content)
            return answers

        else:
            raise WatsonError('Received a status code {code}: {content}  when '
                              'accessing Watson at {url} with username: '
                              '{user}'.format(
                                  code=r.status_code,
                                  content=r.content,
                                  url=conf.watson_url,
                                  user=conf.username))


    def log(self, question, response):
        logging.info('Updating datastore with question.')
        # Insert question into datastore
        answers = response['answers']
        answer = answers[0]['answer'] if len(answers) > 0 else 'No answer given'
        phone_number = int(self.request.get('p', '0'))
        q = Question(phone_number=phone_number,
                     question=question,
                     response=response,
                     answer=answer)
        q.put()

        # Update user stats
        # This isn't atomic, I don't think it's a big deal though.
        user = Stats.query(Stats.phone_number == phone_number).fetch()
        if len(user) > 0:
          user = user[0]
        else:
          user = Stats(phone_number=phone_number,
                       number_of_questions=0,
                       most_recent_question=datetime.min)
        user.number_of_questions += 1
        user.most_recent_question = q.time
        user.put()
