import config

from google.appengine.ext import ndb

class Config(ndb.Model):
  '''Models all configuration information needed for the application to run'''
  
  __DEFAULTS = {'DEFAULT_USERNAME': 'DEFAULT USERNAME',
                'DEFAULT_PASSWORD': 'DEFAULT PASSWORD',
                'DEFAULT_WATSON_URL': 'DEFAULT WATSON URL'}
  
  username = ndb.StringProperty(default=__DEFAULTS['DEFAULT_USERNAME'])
  password = ndb.StringProperty(default=__DEFAULTS['DEFAULT_PASSWORD'])
  watson_url = ndb.StringProperty(default=__DEFAULTS['DEFAULT_WATSON_URL'])

  @classmethod
  def get_master_db(cls):
      return cls.get_or_insert('master')
  
  @classmethod
  def get_defaults(cls):
      return cls.__DEFAULTS
