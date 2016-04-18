from datetime import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.mlb

today = int(datetime.today().strftime("%Y%m%d"))

dates = db.game_dates.find({"date": {"$gt": 20160101,"$lt": today}})
for date in dates:
	dateStr =  str(date['date'])
	year = dateStr[:4]
	month = dateStr[4:6]
	day = dateStr[-2:]
	print year+month+day