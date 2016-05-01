from pymongo import MongoClient
from ConfigParser import SafeConfigParser
import os

def connect():
  parser = SafeConfigParser()
  path = os.path.dirname(os.path.realpath(__file__))
  parser.read(path + '/settings.ini')
  username =  parser.get('mongodb', 'username')
  password =  parser.get('mongodb', 'password')
  
  client = MongoClient()
  db = client.mlb
  db.authenticate(username, password)
  return db



