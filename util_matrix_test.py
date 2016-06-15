from datetime import date
import mongo_connect
import json
import urllib2

db = mongo_connect.connect()



today = date.today()
dateStr =  today.strftime("%Y%m%d")

year = dateStr[:4]
month = dateStr[4:6]
day = dateStr[-2:]
formattedDate = year + "_" + month + "_" + day
url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
scoreboard = json.load(urllib2.urlopen(url))
games = scoreboard['data']['games']['game']
for game in games:
	homeBat = []
	homePit = []
	awayBat = []
	awayPit = []
	home_team = game['home_code']
	away_team= game['away_code']
	gameID = game['gameday_link']

	print gameID
	print home_team + " - " + away_team
	homeRoster = db.rosters.find( { "team": home_team })
	awayRoster = db.rosters.find( { "team": away_team })
	print homeRoster.count()
	print awayRoster.count()
	for player in homeRoster:
		#print player['name'] + " - " + player['pos']
		playerID = str(player['playerID'])
		#print playerID
		if (player['pos'] == 'bat'):
			stats = db.batter_season.find_one({ "playerID": playerID })
			homeBat.append(stats)
		if (player['pos'] == 'pit'):
			stats = db.pitcher_season.find_one({ "playerID": playerID })
			homePit.append(stats)
	for player in awayRoster:
		#print player['name'] + " - " + player['pos']
		playerID = str(player['playerID'])
		#print playerID
		if (player['pos'] == 'bat'):
			stats = db.batter_season.find_one({ "playerID": playerID })
			awayBat.append(stats)
		if (player['pos'] == 'pit'):
			stats = db.pitcher_season.find_one({ "playerID": playerID })
			awayPit.append(stats)
	print len(homeBat)
	print len(homePit)
	print len(awayBat)
	print len(awayPit)
	break

