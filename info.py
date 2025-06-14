import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'FiletoLinkLeoX_Bot')
API_ID = int(environ.get('API_ID', '26696048'))
API_HASH = environ.get('API_HASH', '047b44ea746cab2d97ace09d8988e785')
BOT_TOKEN = environ.get('BOT_TOKEN', "7899034927:AAHa6naHbxlmLYKwkyIQgMEgd5oCxENqwMM")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "7899034927:AAHa6naHbxlmLYKwkyIQgMEgd5oCxENqwMM")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1002884235203'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7664180456 7844061005').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Shakthy:Shakthy10@cluster0.0c015bu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Shakthy")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', ' https://api.gplinks.com/')
SHORTLINK_API = environ.get('SHORTLINK_API', 'ee2ba617e7dd129e04cbdd22322e8d8be5ddbf90')
