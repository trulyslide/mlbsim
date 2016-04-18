from datetime import datetime
import mongo_connect
import json
import urllib2

db = mongo_connect.connect()
today = int(datetime.today().strftime("%Y%m%d"))

dates = db.game_dates.find({"date": {"$gt": 20160101,"$lt": today}})
for date in dates:
	dateStr =  str(date['date'])
	year = dateStr[:4]
	month = dateStr[4:6]
	day = dateStr[-2:]
	url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
	scoreboard = json.load(urllib2.urlopen(url))
	games = scoreboard['data']['games']['game']
	print len(data)
	break
