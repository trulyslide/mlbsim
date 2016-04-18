from datetime import datetime
from pymongo import MongoClient
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('settings.ini')
username =  parser.get('mongodb', 'username')
password =  parser.get('mongodb', 'password')

client = MongoClient()
db = client.mlb
db.authenticate(username, password)

today = int(datetime.today().strftime("%Y%m%d"))

dates = db.game_dates.find({"date": {"$gt": 20160101,"$lt": today}})
for date in dates:
	dateStr =  str(date['date'])
	year = dateStr[:4]
	month = dateStr[4:6]
	day = dateStr[-2:]
	print year+month+day
