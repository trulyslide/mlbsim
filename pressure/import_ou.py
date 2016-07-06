import csv
import mongo_connect

db = mongo_connect.connect()

with open('ou.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        home_team =  row[0]
        gameDate = int(row[1])
        away_team = row[2]
        ou = float(row[3])
        print gameDate
        #game = db.game_log.find_one({'date': gameDate})
        #print game
        db.game_log.update(
        	{
        	'home_team': home_team,
        	'away_team': away_team,
        	'date':gameDate,
        	},
        	{
        	'$set': {'ou': ou}
        	}
        	)
        