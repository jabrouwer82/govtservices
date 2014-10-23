import businesses
import questions
import users
import utils
import watson
import webapp2


class MainPage(utils.Handler):

    def get(self):
        self.render_template('index.html')


application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)

api = webapp2.WSGIApplication([
    ('/api/ask', watson.AskWatson),
    ('/api/users', users.GetUsers),
    ('/api/user', users.AddUser),
    ('/api/questions', questions.GetQuestions),
    ('/api/questions/phone_number', questions.GetQuestionsForPhoneNumber),
    ('/api/business', businesses.AddBusiness)
], debug=True)
