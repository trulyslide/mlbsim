from pymongo import MongoClient

client = MongoClient()
db = client.mlb
cursor = db.teams.find()
for document in cursor:
    print(document['team'])