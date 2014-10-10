Watson 211 WebApp
=================

Web app for the Watson 211 team on the Google App Engine

The app is deployed at [government-services.appspot.com](http://government-services.appspot.com) and is restricted to administrators.

The [/ask](http://government-services.appspot.com/ask) directory can be used to issue a GET request with a 'q' request parameter to ask a question.

For example:
http://government-services.appspot.com/ask?q=How much wood would a woodchuck chuck?

or any HTML compatable version of the above, will issue a POST request to Watson with that question from the uta\_student13 role account if in the deployed version, or form your personal account if locally run.

## Local Authentication

To authenticate with Watson, edit `auth_config.py` with and add your credentials:

    auth = {
        "user": "<your username>",
        "pass": "<your password>"
    }
