from google.appengine.ext import ndb

class Business(ndb.Model):
    '''Models details about businesses.'''

    unique_id = ndb.StringProperty()
    details = ndb.TextProperty()

