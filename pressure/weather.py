from datetime import datetime
import csv
import mongo_connect
import urllib2

db = mongo_connect.connect()

games = db.game_log.find()
for game in games:
	id = game['_id']
	if(game['date'] > 20160101):
		gdate =  str(game['date'])
		print gdate
		year = gdate[:4]
		month = gdate[4:6]
		day = gdate[-2:]
		home_city = game['home_team']
		print home_city
		gtime = game['home_time'] + "PM"
		gtimeDT = datetime.strptime(gtime, '%I:%M%p')
		team = db.teams.find_one({'team': home_city})
		aircode =  team['airport']
		wuLink = "https://www.wunderground.com/history/airport/" + aircode + "/" + year + "/" + month + "/" + day + "/DailyHistory.html?format=1"
		
		weather = urllib2.urlopen(wuLink).read()
		weather = weather.replace("<br />", "")
		weatherList = weather.splitlines()
		weatherList[0:2] = []
		reader = csv.reader(weatherList)
		for row in reader:
			wtime =  str(row[0])
			wtimeDT = datetime.strptime(wtime, '%I:%M %p')
			if(wtimeDT > gtimeDT):
				wtemp = float(row[1])
				if(row[3] != "N/A"):
					whum = float(row[3])
				else:
					whum = ""
				wpres = float(row[4])
				print wtime + " " + str(wpres)
				db.game_log.update(
					{'_id': id},
					{'$set':
					{
						'temp' : wtemp,
						'humidity' : whum,
						'pressure' : wpres
					}
					})
				break