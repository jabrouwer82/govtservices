from google.appengine.ext import ndb

class Question(ndb.Model):
    '''Models details about questions asked by users.'''

    phone_number = ndb.IntegerProperty()
    question = ndb.StringProperty()
    response = ndb.JsonProperty()
    answer = ndb.StringProperty()
    time = ndb.DateTimeProperty(auto_now_add=True)

