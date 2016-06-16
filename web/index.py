#!/usr/bin/python
import cgitb
from pymongo import MongoClient

client = MongoClient()
db = client.mlb

batterSeason = db.batter_season.find({"PA_adj": {"$gt": 2500}}).sort([("OPS_adj", -1)])


cgitb.enable()
print "Content-Type: text/html\n\n"

for season in batterSeason:
	playerID = int(season['playerID'])
	print playerID
	nameQuery = db.rosters.find_one({"playerID":playerID})
	if(nameQuery):
		print nameQuery['name']
	print  " " + str(season['OPS_adj']) + "<br>"

