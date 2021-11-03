import configparser

# CONFIGFILE = '\\\\t110ii\\share\\P\\MSExxx\\95_Automation\\Settings.ini'
CONFIGFILE = 'S:\\MSExxx\\95_Automation\\Settings.ini'

config = configparser.ConfigParser()
config.sections()
config.read(CONFIGFILE)