from google.appengine.ext import ndb

class Business(ndb.Model):
    '''Models details about businesses.'''

    unique_id = ndb.StringProperty()
    details = ndb.TextProperty()
    name = ndb.StringProperty()
    phone_number = ndb.StringProperty()
    url = ndb.StringProperty()
    description = ndb.TextProperty()
    physical_address = ndb.StringProperty()
    mailing_address = ndb.StringProperty()
    taxonomy = ndb.StringProperty()

