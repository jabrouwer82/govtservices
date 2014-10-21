import utils
import watson
import webapp2


class MainPage(utils.Handler):

    def get(self):
        self.render_template('index.html', {})


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/ask', watson.AskWatson)
], debug=True)
