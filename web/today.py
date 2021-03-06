#!/usr/bin/python
import cgitb

from datetime import date

import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

sys.path.append('/var/www/mlbsim')

import mongo_connect

today = date.today()
dateStr =  today.strftime("%Y%m%d")
#dateStr = "20160710"

db = mongo_connect.connect()

cgitb.enable()
print "Content-Type: text/html\n\n"
print "<table>"

games = db.games_prog.find({"date": int(dateStr)})
for game in games:
	homeStarter = game['homeStarter']
	awayStarter = game['awayStarter']
	homeStarterQ = db.rosters.find_one({"playerID":homeStarter,"name": {'$exists':True}})
	awayStarterQ = db.rosters.find_one({"playerID":awayStarter, "name": {'$exists':True}})
	homeStarterName = str(homeStarter)
	awayStarterName = str(awayStarter)
	if (homeStarterQ is not None):
		homeStarterName = homeStarterQ['name']
	if (awayStarterQ is not None):	
		awayStarterName = awayStarterQ['name']

	homeBatters = db.games.find({"pitcherID": awayStarter})
	awayBatters = db.games.find({"pitcherID": homeStarter})

	for batter in homeBatters:
		batterID = batter['batterID']
		#print str(batterID) + " - " + str(awayStarter) + "<br>"
		batterOPS = batter['wOBA_adj']
		nameQuery = db.rosters.find_one({"playerID":batterID})
		if(nameQuery):
			name = nameQuery['name']
		else:
			name = ""
		print "<tr><td>" + str(awayStarter) + "</td><td>"  + awayStarterName + "</td><td>"  + str(batterID) + "</td><td>" + name +  "</td><td>" + str(batterOPS) + "</td></tr>"	

	for batter in awayBatters:
		batterID = batter['batterID']
		batterwOBA = batter['wOBA_adj']
		nameQuery = db.rosters.find_one({"playerID":batterID})
		if(nameQuery):
			name = nameQuery['name']
		else:
			name = ""
		print "<tr><td>" + str(homeStarter) + "</td><td>"  + homeStarterName + "</td><td>"  + str(batterID) + "</td><td>" + name +  "</td><td>" + str(batterwOBA) + "</td></tr>"	


print "</table>"
