import json
import utils

from models.user import User
from google.appengine.api import users
from utils import authenticate


class GetUsers(utils.Handler):
    '''Returns list of up to 20 users.'''

    @authenticate
    def get(self):
        query = User.query()
        list_users = []
        for user_object in query.fetch(limit=20):
            list_users.append({'name': user_object.name,
                               'title': user_object.title,
                               'company': user_object.company})

        output = json.dumps(list_users)
        self.render_json(output)


class AddUser(utils.Handler):
    '''Adds a user to the datastore.'''

    @authenticate
    def post(self):

        request_dict = json.loads(self.request.body)

        user = User(account=users.get_current_user(),
                    name=request_dict.get('name', ''),
                    title=request_dict.get('title', ''),
                    company=request_dict.get('company', ''),
                    admin=(u'on' == request_dict.get('admin', False)))
        user.put()

    @authenticate
    def get(self):
        self.render_template('user.html')
