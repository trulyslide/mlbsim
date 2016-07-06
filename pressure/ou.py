import mongo_connect
db = mongo_connect.connect()

games = db.game_log.find()

for game in games:
	print str(game['date']) + game['home_team']
	id = game['_id']
	home_team_runs = float(game['home_team_runs'])
	away_team_runs = float(game['away_team_runs'])
	ou = game['ou']
	runs = home_team_runs + away_team_runs
	if(runs > ou):
		res = "O"
	if(runs < ou):
		res = "U"
	if(runs == ou):
		res = "P"
	print res
	db.game_log.update(
		{'_id': id},
		{'$set':
		{
			'ouRes' : res
		}
		})