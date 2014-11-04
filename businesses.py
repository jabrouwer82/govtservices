import utils

from datetime import datetime
from models.business import Business
from models.review import Review
from utils import authenticate


class AddBusiness(utils.Handler):
    '''Adds a business to the datastore.'''

    @authenticate
    def post(self):
        business = Business(unique_id=self.request.get('unique_id'),
                            details=self.request.get('details'),
                            name=self.request.get('name'),
                            phone_number=int(self.request.get('phone_number')),
                            url=self.request.get('url'),
                            description=self.request.get('description'),
                            hours=self.request.get('hours'),
                            street_address=self.request.get('street_address'),
                            city=self.request.get('city'),
                            zip_code=self.request.get('zip_code'),
                            image=self.request.get('image'),
                            categories=self.request.get('categories'))
        business.put()

    @authenticate
    def get(self):
        self.render_template('business.html')

class AddReview(utils.Handler):
    '''Adds a review to a business.'''

    @authenticate
    def post(self):
        review = Review(business_id=self.request.get('business_id'),
                        rating=float(self.request.get('rating')),
                        date=datetime.strptime(self.request.get('date'), '%Y-%m-%d'),
                        text=self.request.get('text'))
        review.put()

    @authenticate
    def get(self):
        self.render_template('review.html')
