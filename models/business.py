from google.appengine.ext import ndb

class Business(ndb.Model):
    '''Models details about businesses.'''

    unique_id = ndb.StringProperty()
    details = ndb.TextProperty()
    name = ndb.StringProperty()
    phone_number = ndb.IntegerProperty()
    url = ndb.StringProperty()
    description = ndb.StringProperty()
    hours = ndb.StringProperty()
    street_address = ndb.StringProperty()
    city = ndb.StringProperty()
    zip_code = ndb.StringProperty()
    image = ndb.StringProperty()
    categories = ndb.StringProperty()

