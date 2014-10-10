import auth_config
import base64
import config
import httplib
import json
import logging
import webapp2

from google.appengine.api import urlfetch
from watson_exceptions import ConfigurationError, WatsonError

class AskWatson(webapp2.RequestHandler):
    # Given a question, query Watson for the answer
    # Returns the entire json response
    def get(self):
        # Verify the instance has set a username and password.
        if (auth_config.auth['username'] == config.DEFAULT_USERNAME
              or auth_config.auth['password'] == config.DEFAULT_PASSWORD):
            raise ConfigurationError('Please edit auth_config.py to include '
                                     'your username and password')

        # Standard HTTP basic authorization, base 64 encode username:password
        auth = base64.b64encode(
              '{username}:{password}'.format(
                    username=auth_config.auth['username'],
                    password=auth_config.auth['password']))

         # Load question from request, with a given default.
        question = self.request.get('q', "Where can I find food for my pet?")
        logging.info('Asking Watson: \'{q}\''.format(q=question))
        payload = {
            'question': {
                'questionText': question
            }
        }

        headers = {
            'Authorization': 'Basic {}'.format(auth),
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-SyncTimeout': 30
        }
      
        r = urlfetch.fetch(url=config.WATSON_URL,
                           payload=json.dumps(payload),
                           headers=headers)

        if r.status_code == httplib.OK:
            self.response.write(r.content)
        else:
            raise WatsonError('Received a status code {code}: {status} when '
                              'accessing Watson'.format(
                                    code=r.status_code,
                                    status=httplib.responses[r.status_code]))
