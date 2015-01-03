import utils
import json

from datetime import datetime
from google.appengine.datastore.datastore_query import Cursor
from models.business import Business
from models.review import Review
from utils import authenticate


class GetBusiness(utils.Handler):
    '''Returns a page of up to 10 businesses and a cursos to fetch the next page.'''

    @authenticate
    def get(self):
        curs = Cursor(urlsafe=self.request.get('cursor')) 
        businesses, next_curs, more = Business.query().fetch_page(10, start_cursor=curs)
        list_businesses = []
        for business_object in businesses:
            list_businesses.append(business_object.to_dict())
        ret = {'businesses': list_businesses}
        if more and next_curs:
            ret['cursor'] = next_curs.urlsafe()
        output = json.dumps(ret)
        self.render_json(output)

class AddBusiness(utils.Handler):
    '''Adds a business to the datastore.'''

    @authenticate
    def post(self):
        business = Business(unique_id=self.request.get('unique_id', ''),
                            details=self.request.get('details', ''),
                            name=self.request.get('name', ''),
                            phone_number=self.request.get('phone_number', ''),
                            url=self.request.get('url', ''),
                            description=self.request.get('description', ''),
                            physical_address=self.request.get('physical_address', ''),
                            mailing_address=self.request.get('mailing_address', ''),
                            taxonomy=self.request.get('taxonomy', '')
                           )
        business.put()

    @authenticate
    def get(self):
        self.render_template('business.html')

class AddReview(utils.Handler):
    '''Adds a review to a business.'''

    @authenticate
    def post(self):
        review = Review(business_id=self.request.get('business_id', ''),
                        rating=float(self.request.get('rating', '')),
                        date=datetime.strptime(self.request.get('date', '01-01-0001'),
                                               '%Y-%m-%d'),
                        text=self.request.get('text', ''))
        review.put()

    @authenticate
    def get(self):
        self.render_template('review.html')
