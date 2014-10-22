import json
import utils

from models.user import User


class GetUsers(utils.Handler):
    '''Returns list of up to 20 users.'''

    def get(self):
        query = User.query()
        list_users = []
        for user_object in query.fetch(limit=20):
            list_users.append({'name': user_object.name,
                               'title': user_object.title,
                               'company': user_object.company})

        output = json.dumps(list_users)
        self.render_json(output)
