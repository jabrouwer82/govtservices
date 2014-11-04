from google.appengine.ext import ndb

class Review(ndb.Model):
    '''Models details about a review.'''

    business_id = ndb.StringProperty()
    rating = ndb.FloatProperty()
    date = ndb.DateProperty()
    text = ndb.TextProperty()
