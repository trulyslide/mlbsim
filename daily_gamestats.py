from datetime import datetime
import mongo_connect
import json
import urllib2
import util_gamestats_game

def gamestats():
	db = mongo_connect.connect()
	today = int(datetime.today().strftime("%Y%m%d"))

	latestQ = db.batter_PA.find_one(sort=[("date", -1)])
	latest = latestQ['date']
	latest = int(latest.replace("_", ""))
	print latest

	dates = db.game_dates.find({"date": {"$gt": latest,"$lt": today}})
	for date in dates:
		dateStr =  str(date['date'])
		year = dateStr[:4]
		month = dateStr[4:6]
		day = dateStr[-2:]
		formattedDate = year + "_" + month + "_" + day
		url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
		scoreboard = json.load(urllib2.urlopen(url))
		games = scoreboard['data']['games']['game']
		for game in games:
			game_type = game['game_type']
			status = game['status']
			gameday_link = game['game_data_directory']
			gameID = game['gameday_link']
			print gameID
			if(game_type == "R" and status != "Postponed"):
				gameURL = "http://gd2.mlb.com" + gameday_link + "/inning/inning_all.xml"
				gameData = urllib2.urlopen(gameURL)
				util_gamestats_game.parseGameData(gameData,gameID,formattedDate)
	return "gamestats imported"