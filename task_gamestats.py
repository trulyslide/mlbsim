from datetime import date, timedelta
import mongo_connect
import json
import urllib2
import util_gamestats_game

db = mongo_connect.connect()
yesterday = date.today() - timedelta(1)
print yesterday
dateStr =  yesterday.strftime("%Y%m%d")
print dateStr
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
