from lxml import html
import requests
from bs4 import BeautifulSoup
import boto3

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('mlbsim_teams')
rosterTable = dynamo.Table('mlbsim_rosters')
items = table.scan()
for team in items['Items']:
	teamID = team['team']
	page = requests.get('http://mlb.com/team/roster_40man.jsp?c_id=' + teamID)
	html = page.text
	soup = BeautifulSoup(html,"lxml")
	div40 =  soup.find("div", {"id": "roster_40_man"})
	rows = div40.find_all(lambda tag: tag.name=='tr')

	roster = []

	for row in rows:
	    cols = row.find_all('td')
	    roster.append([ele.contents for ele in cols if ele])
	players = []

	for player in roster:
		if len(player) >0:
			link = BeautifulSoup(str(player[1]),"lxml")
			playerName =  link.find('a').contents[0]
			href = link.find('a').get('href')
			playerID = int(href[-6:])
			#print str(playerID) + " - " + playerName
			rosterTable.put_item(
           		Item={
               		'playerID': playerID,
               		'team': teamID,
               		'name': playerName,
            	}
        	)
	print "Loaded" + teamID