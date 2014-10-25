from google.appengine.ext import ndb

class Stats(ndb.Model):
    '''Models details about app users interactions'''

    phone_number = ndb.IntegerProperty()
    number_of_questions = ndb.IntegerProperty()
    most_recent_question = ndb.DateTimeProperty()

