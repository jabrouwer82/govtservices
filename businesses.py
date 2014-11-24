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
        businesses, next_curs, more = Business.query().fetch_page(5, start_cursor=curs)
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
                            phone_number=int(self.request.get('phone_number', '0')),
                            url=self.request.get('url', ''),
                            description=self.request.get('description', ''),
                            hours=self.request.get('hours', ''),
                            street_address=self.request.get('street_address', ''),
                            city=self.request.get('city', ''),
                            zip_code=self.request.get('zip_code', ''),
                            image=self.request.get('image', ''),
                            categories=self.request.get('categories', '')
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
