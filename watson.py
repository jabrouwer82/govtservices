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

        # Standard HTTP basic authorization, base 64 encode username:password
        auth = 'Basic ' + base64.b64encode(
               '{username}:{password}'.format(
                   username=conf.username,
                   password=conf.password))

        # Load question from request, with a given default.
        question = self.request.get('q', 'Where can I find food for my pet?')
        logging.info("Asking Watson: '{q}'".format(q=question))
        payload = {
            'question': {
                'questionText': question
            }
        }

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
            
            answers = self.format_answer(r)

            log = self.request.get('l')
            if log:
              self.log(question, answers)

            self.render_json(json.dumps(answers))
        else:
            raise WatsonError('Received a status code {code}: {status} when '
                              'accessing Watson at {url} with username: '
                              '{user}'.format(
                                  code=r.status_code,
                                  status=httplib.responses[r.status_code],
                                  url=conf.watson_url,
                                  user=conf.username))

    def format_answer(self, r):
        watson_response = json.loads(r.content)
        answers = {}
        answers['answers'] = []
        for x in xrange(3):
            text = watson_response['question']['answers'][x]
            document = watson_response['question']['evidencelist'][x]['metadataMap']['title']
            service_name = document.split(' : ')[1]
            services = Business.query(Business.name == service_name).fetch()
            service = services[0].to_dict() if len(services) > 0 else []
            answer = {'answer': text,
                      'service': service,
                      'id': x
                     }
            answers['answers'].append(answer)
        return answers


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
