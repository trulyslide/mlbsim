#!/usr/bin/python
import cgitb
from sim import mongo_connect
from datetime import date

today = date.today()
dateStr =  today.strftime("%Y%m%d")

db = mongo_connect.connect()

cgitb.enable()
print "Content-Type: text/html\n\n"
print "<table>"

games = db.games_prog.find({"date": 20160615})

for game in games:
	homeStarter = game['homeStarter']
	awayStarter = game['awayStarter']

	homeStarterQ = db.rosters.find_one({"playerID":homeStarter})
	awayStarterQ = db.rosters.find_one({"playerID":awayStarter})
	homeStarterName = str(homeStarter)
	awayStarterName = str(awayStarter)
	if (homeStarterQ):
		homeStarterName = homeStarterQ['name']
	if (awayStarterQ):	
		awayStarterName = awayStarterQ['name']

	homeBatters = db.games.find({"pitcherID": str(awayStarter)})
	awayBatters = db.games.find({"pitcherID": str(homeStarter)})
	#print str(homeBatters.count()) + "<br>"
	#print str(awayBatters.count()) + "<br>"

	for batter in homeBatters:
		batterID = batter['batterID']
		#print str(batterID) + " - " + str(awayStarter) + "<br>"
		batterOPS = batter['OPS_adj']
		nameQuery = db.rosters.find_one({"playerID":int(batterID)})
		if(nameQuery):
			name = nameQuery['name']
		else:
			name = ""
		print "<tr><td>" + str(awayStarter) + "</td><td>"  + awayStarterName + "</td><td>"  + str(batterID) + "</td><td>" + name +  "</td><td>" + str(batterOPS) + "</td></tr>"	

	for batter in awayBatters:
		batterID = batter['batterID']
		batterOPS = batter['OPS_adj']
		nameQuery = db.rosters.find_one({"playerID":int(batterID)})
		if(nameQuery):
			name = nameQuery['name']
		else:
			name = ""
		print "<tr><td>" + str(homeStarter) + "</td><td>"  + homeStarterName + "</td><td>"  + str(batterID) + "</td><td>" + name +  "</td><td>" + str(batterOPS) + "</td></tr>"	


print "</table>"
