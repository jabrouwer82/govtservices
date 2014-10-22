# Application-wide configuration constants
import models.config
import os

# Default configuration settings.
CONFIG_DEFAULTS = models.config.Config.get_defaults()

# Actual configuration settings.
CONFIG_DB = models.config.Config.get_master_db()

# Which server am I?
DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')
PROD = not DEV
