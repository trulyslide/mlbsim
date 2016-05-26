import MySQLdb
import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.mlb
from datetime import datetime

#find last updated date from mongo
dataStatus = db.status.find()
for data in dataStatus:
	lastDateUpdated = data['dateUpdated']
	print lastDateUpdated

#today's date
now = datetime.now()
today = str(now.strftime("%Y_%m_%d"))

#get rows where date > lastDateUpdated
batterPAs = db.batter_PA.find( { "date": {"$gt": lastDateUpdated }} ).sort([("date", 1),("playerID", 1)])
lastPADate = ""
for pa in batterPAs:
	paDate =  pa['date']
	playerID = pa['playerID']
	if(paDate != lastPADate):
		print paDate
	lastPADate = paDate
	print playerID



#process code

#update mongo with last processed date
