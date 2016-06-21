from lxml import html
import requests
from bs4 import BeautifulSoup
import mongo_connect
from ConfigParser import SafeConfigParser
import datetime
today = datetime.date.today()

db = mongo_connect.connect()

db.rosters.remove()

batters = requests.get('http://gd2.mlb.com/components/game/mlb/year_2016/batters/').text
pitchers = requests.get('http://gd2.mlb.com/components/game/mlb/year_2016/pitchers/').text
items = db.teams.find()
for team in items:
	teamID = team['team']
	webID = team['webID']
	page = requests.get('http://mlb.com/team/roster_active.jsp?c_id=' + webID)
	html = page.text
	soup = BeautifulSoup(html,"lxml")
	div40 =  soup.find("div", {"id": "content"})
	rows = div40.find_all(lambda tag: tag.name=='tr')

	roster = []

	for row in rows:
	    cols = row.find_all('td')
	    roster.append([ele.contents for ele in cols if ele])
	print len(roster)
	players = []

	for player in roster:
		#print player
		if len(player) >0:
			link = BeautifulSoup(str(player[2]),"lxml")
			#print link
			playerName =  link.find('a').contents[0]
			href = link.find('a').get('href')
			playerIDstr = href[8:14]
			playerID = int(playerIDstr)
			if playerIDstr in batters:
				pos = "bat"
			if playerIDstr in pitchers:
				pos = "pit"
			bt = str(BeautifulSoup(str(player[3]),"lxml").get_text())
			bats = bt[3]
			throws = bt[-3]
			print bats
			print throws
			#print str(playerID) + " - " + playerName
			db.rosters.update(
           		{
           		'playerID': playerID,
               		'team': teamID
           		},
           		{
               		'playerID': playerID,
               		'team': teamID,
               		'name': playerName,
               		'pos' : pos,
               		'bats': bats,
               		'throws': throws
            	},
            	upsert=True)
	print "Loaded" + teamID
