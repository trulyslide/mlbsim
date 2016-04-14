
import MySQLdb
from pymongo import MongoClient

client = MongoClient()
dbMongo = client.mlb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="mlb",         # your username
                     passwd="mlb",  # your password
                     db="mlb")        # name of the data base

cur = db.cursor()
cur.execute("SELECT * FROM gd_atbat2015 GROUP BY batter")
i=1
for row in cur.fetchall():
    batterID = int(row[2])
    batter_name = str(row[24])
    result = dbMongo.batters.insert_one(
    {
        "playerID" : batterID,
        "batter_name" : batter_name
    })
    print i
    i+=1
db.close()