Watson 211 WebApp
=================

Web app for the Watson 211 team on the Google App Engine

The app is deployed at [government-services.appspot.com](http://government-services.appspot.com) and is restricted to administrators.

The [/ask](http://government-services.appspot.com/ask) directory can be used to issue a GET request with a 'q' request parameter to ask a question.

For example:
http://government-services.appspot.com/ask?q=How much wood would a woodchuck chuck?

or any HTML compatable version of the above, will issue a POST request to Watson with that question from the uta\_student13 role account if in the deployed version, or form your personal account if locally run.

## Configuration

All configuration settings are now stored in the datastore, in a Config model. This allows up to update the watson url or login credentials without having to redeploy the application. To edit the production configuration, go to [the datastore viewer](https://appengine.google.com/datastore/explorer?&app_id=s~government-services)  and navigate to the Config model, the edit the master record to have the appropriate values.

To configure the application locally, launch the application and open the /ask page (this will cause the configurations to get written to the database) then open the [local datastore viewer](http://localhost:8000/datastore?kind=Config) and change the settings shown to your username, password, and watson url. You might have to do this repeatedly while developing the app, if this happens and/or becomes a pain, we can look for a work around.

After changing the configuration, be sure to flush the memcache to make the application notice your changes sooner. It still might take a minute or two for them to update though. If the settings don't update quickly enough for your taste, stoping and starting the application will guarantee an update.  When editing the prod configurations, you will need to shutdown all the instances in order fr the new values to be read correctly.

Be sure to check the "Sign in as Administrator" button to have site access. Signing out of a test account can be a pain in the ass, a proper signout page will be added later to address this. For now it is recommended that you view your local server from private/incognito mode to avoid these issues.

## Deploying the application

It is recommended that before you deploy the application, you increment the app version in app.yaml, this allows us to easily roll back the change in case of an issue. The current versioning set up is: 1-2-1 (major-minor-maintainance) because app engine does not allow for periods in version numbers.

Deploying shouldn't take too long, however it should be noted that on my ocal machine and home internet it take between 10 and 20 minutes, so be patient with it.

After the deploy is successful, be sure to open the [admin console](https://appengine.google.com/dashboard?&app_id=s~government-services) and change the default version form the old to the new in order to make the changes live.
