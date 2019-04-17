from everett.ext.inifile import ConfigIniEnv
from everett.manager import ConfigManager, ConfigOSEnv


def read_config(config_path: str):
    """
    Read the configuration from the config ini file given.
    :return:
    """
    return ConfigManager(
        # Specify one or more configuration environments in
        # the order they should be checked
        environments=[
            # Look in OS process environment first
            ConfigOSEnv(),

            # Look in INI file given in parameter
            ConfigIniEnv([config_path]),
        ],

        # Provide users a link to documentation for when they hit
        # configuration errors
        doc='Check https://example.com/configuration for docs.'
    )