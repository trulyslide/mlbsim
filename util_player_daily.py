import MySQLdb
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

dynamo = boto3.resource('dynamodb')
tableBat = dynamo.Table('mlbsim_batters')
tablePit = dynamo.Table('mlbsim_pitchers')
tableBatPA = dynamo.Table('mlbsim_batter_PA')
tablePitPA = dynamo.Table('mlbsim_pitcher_PA')
tableBatDaily = dynamo.Table('mlbsim_batter_daily')
tablePitDaily = dynamo.Table('mlbsim_pitcher_daily')
gameDatePrev = "";
events = {}
def reset(events):
	events['AB'] = 0
	events['1B'] = 0
	events['2B'] = 0
	events['3B'] = 0
	events['HR'] = 0
	events['H'] = 0
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

def loadDate(events,playerID):
	eventDate = events['date']
	dateObject = datetime.strptime(eventDate, '%Y_%m_%d')
	dynamoDate = int(dateObject.strftime('%Y%m%d'))
	tableBatDaily.put_item(
        Item={
            'playerID': playerID,
            'date' : dynamoDate,
            'AB' : events['AB'],
			'1B' : events['1B'],
			'2B' : events['2B'],
			'3B' : events['3B'],
			'HR' : events['HR'],
			'H' : events['H'],
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
        }
    )
reset(events)
batters = tableBat.scan()
i = 0
for batter in batters['Items']:
	i+=1
	print i
	playerID = batter['playerID']
	print playerID
	batterPAs = tableBatPA.query(
    	KeyConditionExpression=Key('playerID').eq(playerID)
    	)
	#print batterPAs['LastEvaluatedKey']
	for pa in batterPAs['Items']:
		gameDate = pa['date']
		if(gameDate != gameDatePrev and gameDatePrev != ""):
			loadDate(events,playerID)
			events = reset(events)
		events['date'] = gameDate
		gameDatePrev = gameDate
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
	loadDate(events,playerID)