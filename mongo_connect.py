from pymongo import MongoClient
from ConfigParser import SafeConfigParser

def connect():
  parser = SafeConfigParser()
  parser.read('settings.ini')
  username =  parser.get('mongodb', 'username')
  password =  parser.get('mongodb', 'password')
  
  client = MongoClient()
  db = client.mlb
  db.authenticate(username, password)
  return db



