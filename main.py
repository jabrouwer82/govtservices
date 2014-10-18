import webapp2
import watson
import utils


class MainPage(utils.Handler):

    def get(self):
        self.render_template('index.html', {})


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/ask', watson.AskWatson)
], debug=True)
