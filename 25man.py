from lxml import html
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.mlb

db.rosters.remove( { } )

items = db.teams.find()
for team in items:
	teamID = team['team']
	page = requests.get('http://mlb.com/team/roster_active.jsp?c_id=' + teamID)
	html = page.text
	soup = BeautifulSoup(html,"lxml")
	div40 =  soup.find("div", {"id": "content"})
	rows = div40.find_all(lambda tag: tag.name=='tr')

	roster = []

	for row in rows:
	    cols = row.find_all('td')
	    roster.append([ele.contents for ele in cols if ele])
	players = []

	for player in roster:
		#print player
		if len(player) >0:
			link = BeautifulSoup(str(player[2]),"lxml")
			#print link
			playerName =  link.find('a').contents[0]
			href = link.find('a').get('href')
			playerID = int(href[8:14])
			#print str(playerID) + " - " + playerName
			db.rosters.insert_one(
           		{
               		'playerID': playerID,
               		'team': teamID,
               		'name': playerName,
            	}
        	)
	print "Loaded" + teamID