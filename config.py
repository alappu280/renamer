import re, os
from time import time

id_pattern = re.compile(r'^.\d+$') 

BOT_START_TIME = time()

API_ID = os.environ.get("API_ID", "9254436")

API_HASH = os.environ.get("API_HASH", "42665ffe4407fbc3f59c412caa9d84d3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925633630:AAGKwXs05MD4TtTUTQbgmzZPymXlX7UZseI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MLZ_BOTZ") 

DB_NAME = os.environ.get("DB_NAME","irfanmama")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://irfanmama:irfanmama@cluster0.amfvame.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1833209093 5845960615 5596825598').split()]

PORT = os.environ.get('PORT', '8080')

LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001898159090'))
