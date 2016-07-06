import mongo_connect
db = mongo_connect.connect()

games = db.game_log.find()

overs = 0
unders = 0
overPressure = 0
underPressure = 0
overHum = 0
underHum = 0
overTemp = 0
underTemp = 0
oTot = 0
uTot = 0

for game in games:
	#print str(game['date']) + game['home_team']
	home = game['home_team']
	runs = game['home_team_runs'] + game['away_team_runs']
	res = game['ouRes']
	ou = game['ou']
	pressure = game['pressure']
	hum = game['humidity']
	temp = game['temp']
	if(ou == 6.5):
		print home
		if(res == "O"):
			overs = overs + 1
			overPressure = overPressure + pressure
			overHum = overHum + hum
			overTemp = overTemp + temp
			oTot = oTot + ou
		if(res == "U"):
			unders = unders + 1 
			underPressure = underPressure + pressure
			underHum = underHum + hum
			underTemp = underTemp + temp
			uTot = uTot + ou

overAvg = 0
overAvgH = 0
overAvgT = 0
underAvg = 0
underAvgH = 0
underAvgT = 0

if(overs > 0):
	overAvg = overPressure / overs
	overAvgH = overHum / overs
	overAvgT = overTemp / overs
if(unders > 0):
	underAvg = underPressure / unders
	underAvgH = underHum / unders
	underAvgT = underTemp / unders

print "Overs: Total - " + str(overs) + " Temp - " + str(overAvgT)  + " Pressure - " + str(overAvg) + " Humidity - " + str(overAvgH)
print "Unders: Total - " + str(unders) + " Temp - " + str(underAvgT) + " Pressure - " + str(underAvg)	+ " Humidity - " + str(underAvgH)	
print str(oTot/overs) + "-" + str(uTot/unders)	
