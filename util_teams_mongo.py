import boto3
from pymongo import MongoClient
client = MongoClient()
db = client.mlb
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('mlbsim_teams')

items = table.scan()
for team in items['Items']:
	teamID = team['team']
	city = team['city']
	division = team['division']
	league = team['league']
	nickname = team['nickname']

	db.teams.insert_one(
        {
            'team': teamID,
            'city' : city,
            'division' : division,
			'league' : league,
			'nickname' : nickname
		}
	)