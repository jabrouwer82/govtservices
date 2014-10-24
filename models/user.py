from google.appengine.ext import ndb

class User(ndb.Model):
    '''Models a user.'''

    account = ndb.UserProperty()
    name = ndb.StringProperty()
    title = ndb.StringProperty()
    company = ndb.StringProperty()
    admin = ndb.BooleanProperty()

