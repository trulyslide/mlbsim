import MySQLdb
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.mlb

today = str(datetime.date.today())
dateObject = datetime.datetime.strptime(today, '%Y-%m-%d')
dynamoDate = int(dateObject.strftime('%Y%m%d'))
print dynamoDate
dates = db.game_dates.find({"date": { "$lt": dynamoDate } }).sort([("date", -1)])
i=100
for date in dates:
	print date['date']
	db.game_dates.update( { 'date':date['date'] }, { '$set' : { 'weight':i } } ) 
	if(i>0):
		i-=1
	