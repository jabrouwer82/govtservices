# Application-wide configuration constants
import models.config

# Default configuration settings.
CONFIG_DEFAULTS = models.config.Config.get_defaults()

# Actual configuration settings.
CONFIG_DB = models.config.Config.get_master_db()
