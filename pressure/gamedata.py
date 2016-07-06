from datetime import datetime
import mongo_connect
import json
import urllib2
db = mongo_connect.connect()

#db.game_log.remove({})
todayStr = datetime.today().strftime("%Y%m%d")
today = int(todayStr)
gamedates = db.game_dates.find({"date": {"$gt": 20160101,"$lt": today}})

for gamedate in gamedates:
	dateStr =  str(gamedate['date'])
	year = dateStr[:4]
	month = dateStr[4:6]
	day = dateStr[-2:]
	formattedDate = year + "_" + month + "_" + day
	url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
	print url
	scoreboard = json.load(urllib2.urlopen(url))
	games = scoreboard['data']['games']['game']
	for game in games:
		home_team = game['home_code']
		away_team= game['away_code']
		if(game['status'] == "Final"):
			home_team_runs = int(game['home_team_runs'])
			away_team_runs = int(game['away_team_runs'])
			home_time = game['home_time']
			print dateStr
			db.game_log.insert({
				"date" : gamedate['date'],
				"home_team" : home_team,
				"away_team" : away_team,
				"home_team_runs" : home_team_runs,
				"away_team_runs" : away_team_runs,
				"home_time" : home_time
				})