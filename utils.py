# This file contains helpful "tools" that other files can import and use
import jinja2
import os
import webapp2
import config

from watson_exceptions import AuthenticationError

jinja_environment = jinja2.Environment(
    autoescape=True,
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')
    )
)


class Handler(webapp2.RequestHandler):
    """General request handler including helper methods and other general
    handling"""

    def render_template(self, template_name, contents):
        """Helper method to render the template with the appropriate contents.

        :type template_name: string
        :param template_name: filepath of template in templates directory
        :type contents: dict
        :param contents: key/values to populate the template

        :rtype: None
        """
        # TODO(matthewe|2014-10-16): Add 404 functionality if template
        # not found
        template = jinja_environment.get_template(template_name)
        self.response.out.write(template.render(contents))

    def render_json(self, json_txt):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json_txt)


def is_authenticated(request):
    '''This is a super shitty authentication, and desperatly needs to be migrated to something the resembles something secure before this goes public.'''
    # Don't worry about auth if in local DEV mode
    if config.DEV:
        return True
    # If our secret z bit is set
    elif request.get('z') == '1':
        return True
    else:
        return False

def authenticate(func):
    def authenticate_and_call(self):
        if not is_authenticated(self.request): 
            raise AuthenticationError('Unable to authenticate request. Please try again with the appropriate credentials.')
        return func(self)
    return authenticate_and_call
