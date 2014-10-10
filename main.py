import webapp2
import watson

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('hello, world')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/ask', watson.AskWatson)
], debug=True)
