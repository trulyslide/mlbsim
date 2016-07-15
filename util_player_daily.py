import datetime
import mongo_connect

db = mongo_connect.connect()
from datetime import datetime

db.pitcher_PA_daily.remove()
db.batter_PA_daily.remove()
events = {}
def reset(events):
	events['AB'] = 0
	events['1B'] = 0
	events['2B'] = 0
	events['3B'] = 0
	events['HR'] = 0
	events['H'] = 0
	events['1Bfac'] = 0
	events['2Bfac'] = 0
	events['3Bfac'] = 0
	events['HRfac'] = 0
	events['Hfac'] = 0
	events['BInf'] = 0
	events['GndO'] = 0
	events['Bunt'] = 0
	events['LinO'] = 0
	events['PopO'] = 0
	events['FC'] = 0
	events['FlyO'] = 0
	events['DP'] = 0
	events['K'] = 0
	events['TP'] = 0
	events['CInf'] = 0
	events['FInf'] = 0
	events['E'] = 0
	events['HBP'] = 0
	events['IBB'] = 0
	events['BB'] = 0
	events['Sac'] = 0
	return events

def loadDateBatter(events,playerID):
	eventDate = events['date']
	dateObject = datetime.strptime(eventDate, '%Y_%m_%d')
	dynamoDate = int(dateObject.strftime('%Y%m%d'))
	db.batter_PA_daily.update(
		{
			'playerID': playerID,
			'date' : dynamoDate,
			'throws' : events['throws']
		},
		{
			'playerID': playerID,
			'date' : dynamoDate,
			'throws' : events['throws'],
			'AB' : events['AB'],
			'1B' : events['1B'],
			'2B' : events['2B'],
			'3B' : events['3B'],
			'HR' : events['HR'],
			'H' : events['H'],
			'1Bfac' : events['1Bfac'],
			'2Bfac' : events['2Bfac'],
			'3Bfac' : events['3Bfac'],
			'HRfac' : events['HRfac'],
			'Hfac' : events['Hfac'],
			'BInf' : events['BInf'],
			'GndO' : events['GndO'],
			'Bunt' : events['Bunt'],
			'LinO' : events['LinO'],
			'PopO' : events['PopO'],
			'FC' : events['FC'],
			'FlyO' : events['FlyO'],
			'DP' : events['DP'],
			'K' : events['K'],
			'TP' : events['TP'],
			'CInf' : events['CInf'],
			'FInf' : events['FInf'],
			'E' : events['E'],
			'HBP' : events['HBP'],
			'IBB' : events['IBB'],
			'BB' : events['BB'],
			'Sac' : events['Sac']
		},
		upsert=True)

def loadDatePitcher(events,playerID):
	eventDate = events['date']
	dateObject = datetime.strptime(eventDate, '%Y_%m_%d')
	dynamoDate = int(dateObject.strftime('%Y%m%d'))
	db.pitcher_PA_daily.update(
		{
			'playerID': playerID,
			'date' : dynamoDate,
			'stand' : events['stand']
		},
		{
			'playerID': playerID,
			'date' : dynamoDate,
			'stand' : events['stand'],
			'AB' : events['AB'],
			'1B' : events['1B'],
			'2B' : events['2B'],
			'3B' : events['3B'],
			'HR' : events['HR'],
			'H' : events['H'],
			'1Bfac' : events['1Bfac'],
			'2Bfac' : events['2Bfac'],
			'3Bfac' : events['3Bfac'],
			'HRfac' : events['HRfac'],
			'Hfac' : events['Hfac'],
			'BInf' : events['BInf'],
			'GndO' : events['GndO'],
			'Bunt' : events['Bunt'],
			'LinO' : events['LinO'],
			'PopO' : events['PopO'],
			'FC' : events['FC'],
			'FlyO' : events['FlyO'],
			'DP' : events['DP'],
			'K' : events['K'],
			'TP' : events['TP'],
			'CInf' : events['CInf'],
			'FInf' : events['FInf'],
			'E' : events['E'],
			'HBP' : events['HBP'],
			'IBB' : events['IBB'],
			'BB' : events['BB'],
			'Sac' : events['Sac']
		},
		upsert=True)

reset(events)

#find last updated date from mongo
dataStatus = db.status.find()
for data in dataStatus:
	lastDateUpdated = data['dateUpdated']
	print lastDateUpdated

#get rows where date > lastDateUpdated
batterPAs = db.batter_PA.find( { "date": {"$gt": lastDateUpdated }} ).sort([("date", 1),("playerID", 1),("throws", 1)])
pitcherPAs = db.pitcher_PA.find( { "date": {"$gt": lastDateUpdated }} ).sort([("date", 1),("playerID", 1),("stand", 1)])
print batterPAs.count()
print pitcherPAs.count()
lastPADate = ""
lastPlayerID = ""
lastStand = ""
for pa in pitcherPAs:
	paDate =  pa['date']
	playerID = pa['playerID']
	stand = pa['stand']
	gameID = pa['gamelink_num']
	parts = gameID.split("_")
	park = parts[-2][:3]
	factors = db.factors.find_one({"team": park, "stand": stand})
	facHR = factors['HR']
	fac1B = factors['1B']
	fac2B = factors['2B']
	fac3B = factors['3B']
	events['date'] = paDate
	if((paDate != lastPADate or playerID != lastPlayerID or stand != lastStand) and lastPlayerID != ""):
		print paDate
		print playerID
		events['HRfac'] = events['HR'] / facHR
		events['1Bfac'] = events['1B'] / fac1B
		events['2Bfac'] = events['2B'] / fac2B
		events['3Bfac'] = events['3B'] / fac3B
		events['Hfac'] = events['HRfac'] + events['1Bfac'] + events['2Bfac'] + events['3Bfac']
		loadDatePitcher(events,lastPlayerID)
		events = reset(events)
	lastPADate = paDate
	lastPlayerID = playerID
	lastStand = stand
	events['stand'] = stand
	event = pa['event']
	if event == "Single":
		events['AB'] += 1
		events['1B'] += 1
		events['H'] += 1
	if event == "Double":
		events['AB'] += 1
		events['2B'] += 1
		events['H'] += 1
	if event == "Triple":
		events['AB'] += 1
		events['3B'] += 1
		events['H'] += 1
	if event == "Home Run":
		events['AB'] += 1
		events['HR'] += 1
		events['H'] += 1
	if event == "Batter Interference":
		events['AB'] += 1
		events['BInf'] += 1
	if "Bunt" in event:
		events['Bunt'] += 1
	if "Groundout" in event:
		events['GndO'] += 1
		events['AB'] += 1
	if "Lineout" in event:
		events['LinO'] += 1
		events['AB'] += 1
	if "Pop Out" in event:
		events['PopO'] += 1
		events['AB'] += 1
	if "Pop Out" in event:
		events['PopO'] += 1
		events['AB'] += 1
	if "Double Play" in event:
		events['GndO'] += 1
		events['DP'] += 1
		events['AB'] += 1
	if "Triple Play" in event:
		events['GndO'] += 1
		events['TP'] += 1
		events['AB'] += 1
	if "Fielders Choice" in event:
		events['GndO'] += 1
		events['FC'] += 1
		events['AB'] += 1
	if "Flyout" in event:
		events['FlyO'] += 1
		events['AB'] += 1
	if "Forceout" in event:
		events['GndO'] += 1
		events['AB'] += 1
	if event == "Grounded Into DP":
		events['DP'] += 1
		events['GndO'] += 1
		events['AB'] += 1
	if "Strikeout" in event:
		events['K'] += 1
		events['AB'] += 1
	if event == "Catcher Interference":
		events['CInf'] += 1
	if event == "Fan Interference":
		events['FInf'] += 1
	if "Error" in event:
		events['E'] += 1
	if "Hit By Pitch" in event:
		events['HBP'] += 1
	if "Intent Walk" in event:
		events['IBB'] += 1
		events['BB'] += 1
	if "Walk" in event:
		events['BB'] += 1
	if "Sac" in event:
		events['Sac'] += 1
events['HRfac'] = events['HR'] / facHR
events['1Bfac'] = events['1B'] / fac1B
events['2Bfac'] = events['2B'] / fac2B
events['3Bfac'] = events['3B'] / fac3B
events['Hfac'] = events['HRfac'] + events['1Bfac'] + events['2Bfac'] + events['3Bfac']
loadDatePitcher(events,lastPlayerID)

lastPADate = ""
lastPlayerID = ""
lastThrows = ""
for pa in batterPAs:
	paDate =  pa['date']
	playerID = pa['playerID']
	throws = pa['p_throws']
	gameID = pa['gamelink_num']
	parts = gameID.split("_")
	park = parts[-2][:3]
	factors = db.factors.find_one({"team": park, "stand": stand})
    	facHR = factors['HR']
    	fac1B = factors['1B']
    	fac2B = factors['2B']
    	fac3B = factors['3B']
	if((paDate != lastPADate or playerID != lastPlayerID or throws != lastThrows) and lastPlayerID != ""):
		events['HRfac'] = events['HR'] / facHR
		events['1Bfac'] = events['1B'] / fac1B
		events['2Bfac'] = events['2B'] / fac2B
		events['3Bfac'] = events['3B'] / fac3B
		events['Hfac'] = events['HRfac'] + events['1Bfac'] + events['2Bfac'] + events['3Bfac']
		loadDateBatter(events,lastPlayerID)
		events = reset(events)
		print playerID
		print paDate
	events['date'] = paDate
	lastPADate = paDate
	lastPlayerID = playerID
	lastThrows = throws
	events['throws'] = throws
	event = pa['event']
	if event == "Single":
		events['AB'] += 1
		events['1B'] += 1
		events['H'] += 1
	if event == "Double":
		events['AB'] += 1
		events['2B'] += 1
		events['H'] += 1
	if event == "Triple":
		events['AB'] += 1
		events['3B'] += 1
		events['H'] += 1
	if event == "Home Run":
		events['AB'] += 1
		events['HR'] += 1
		events['H'] += 1
	if event == "Batter Interference":
		events['AB'] += 1
		events['BInf'] += 1
	if "Bunt" in event:
		events['Bunt'] += 1
	if "Groundout" in event:
		events['GndO'] += 1
		events['AB'] += 1
	if "Lineout" in event:
		events['LinO'] += 1
		events['AB'] += 1
	if "Pop Out" in event:
		events['PopO'] += 1
		events['AB'] += 1
	if "Pop Out" in event:
		events['PopO'] += 1
		events['AB'] += 1
	if "Double Play" in event:
		events['GndO'] += 1
		events['DP'] += 1
		events['AB'] += 1
	if "Triple Play" in event:
		events['GndO'] += 1
		events['TP'] += 1
		events['AB'] += 1
	if "Fielders Choice" in event:
		events['GndO'] += 1
		events['FC'] += 1
		events['AB'] += 1
	if "Flyout" in event:
		events['FlyO'] += 1
		events['AB'] += 1
	if "Forceout" in event:
		events['GndO'] += 1
		events['AB'] += 1
	if event == "Grounded Into DP":
		events['DP'] += 1
		events['GndO'] += 1
		events['AB'] += 1
	if "Strikeout" in event:
		events['K'] += 1
		events['AB'] += 1
	if event == "Catcher Interference":
		events['CInf'] += 1
	if event == "Fan Interference":
		events['FInf'] += 1
	if "Error" in event:
		events['E'] += 1
	if "Hit By Pitch" in event:
		events['HBP'] += 1
	if "Intent Walk" in event:
		events['IBB'] += 1
		events['BB'] += 1
	if "Walk" in event:
		events['BB'] += 1
	if "Sac" in event:
		events['Sac'] += 1
events['HRfac'] = events['HR'] / facHR
events['1Bfac'] = events['1B'] / fac1B
events['2Bfac'] = events['2B'] / fac2B
events['3Bfac'] = events['3B'] / fac3B
events['Hfac'] = events['HRfac'] + events['1Bfac'] + events['2Bfac'] + events['3Bfac']
loadDateBatter(events,lastPlayerID)

result = db.status.update(
{
	"year" : 2016
},
{
	"year" : 2016,
	"dateUpdated" : paDate
},
upsert=True)
