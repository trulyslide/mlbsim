import mongo_connect
db = mongo_connect.connect()

batterPAs = db.batter_PA.find( { "date": {"$gt": '2015_01_01' }} ).sort([("date", 1),("playerID", 1)])
for pa in batterPAs:
  stand = pa['stand']
  gameID = pa['gamelink_num']
  parts = gameID.split("_")
  park = parts[5][:3]
  factors = db.factors.find_one({"team": park, "stand": stand})
  facHR = factors['HR']
  fac1B = factors['1B']
  fac2B = factors['2B']
  fac3B = factors['3B']
      
  print gameID + park + stand + str(facHR)
  break
