import mongo_connect

db = mongo_connect.connect()

pitcherPAs =db.pitcher_PA.find({ "park" : { "$exists" : False } })
for pa in pitcherPAs:
	gameID = pa['gamelink_num']
	print gameID
	parts = gameID.split("_")
	park = parts[5][:3]
	
	db.batter_PA.update(
		{
			'gamelink_num': gameID
		},
		{ '$set': {
			'park':park
		}})