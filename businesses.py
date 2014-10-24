import utils

from models.business import Business
from utils import authenticate


class AddBusiness(utils.Handler):
    '''Adds a business to the datastore.'''

    @authenticate
    def post(self):
        business = Business(unique_id=self.request.get('unique_id'),
                            details=self.request.get('details'))
        business.put()

    @authenticate
    def get(self):
        self.render_template('business.html')
