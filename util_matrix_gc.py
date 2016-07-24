from datetime import date
import mongo_connect
import json
import urllib2
import xml.etree.cElementTree as ET

db = mongo_connect.connect()

db.games_prog.remove({})

homeBat = []
homePit = []
awayBat = []
awayPit = []

today = date.today()
dateStr =  today.strftime("%Y%m%d")
#dateStr = "20160710"

year = dateStr[:4]
month = dateStr[4:6]
day = dateStr[-2:]
formattedDate = year + "_" + month + "_" + day
url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
scoreboard = json.load(urllib2.urlopen(url))
games = scoreboard['data']['games']['game']
for game in games:
	home_team = game['home_code']
	away_team= game['away_code']
	gameID = game['gameday_link']
	print gameID
	gcLink = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/gid_" + gameID + "/gamecenter.xml"
	urlData = urllib2.urlopen(gcLink)
	try:
		gcData = ET.parse(urllib2.urlopen(gcLink)).getroot()
		for child in gcData.getchildren():
			if child.tag == 'probables':
				for child2 in child.getchildren():
					if child2.tag == 'home':
						for child3 in child2.getchildren():
							if child3.tag == 'player_id':
								print child3.text
								homeStarter = child3.text
							if child3.tag == 'throwinghand':
								if(child3.text == "RHP"):
									throws = "R"
								if(child3.text == "LHP"):
									throws = "L"
					if child2.tag == 'away':
						for child3 in child2.getchildren():
							if child3.tag == 'player_id':
								print child3.text
								awayStarter = child3.text
		
		if(awayStarter == None):
			awayStarter = 0
		if(homeStarter == None):
			homeStarter = 0
			
		db.rosters.update(
		{
			"playerID": awayStarter,
			"team": away_team
		},
		{
			"playerID": awayStarter,
			"team": away_team,
			"pos": "pit",
			"throws": throws
		},
	        upsert=True)
		db.rosters.update(
		{
			"playerID": homeStarter,
			"team": home_team
		},
		{
			"playerID": homeStarter,
			"team": home_team,
			"pos": "pit",
			"throws": throws
		},
	    	upsert=True)
				
		awayStarterLookup = db.pitcher_season.find_one({"playerID":int(awayStarter)})
		if(awayStarterLookup is None):
			print "insert blank"
			db.pitcher_season.insert(
				{
				"playerID" : int(awayStarter),
				'stand' : 'L',
				'AB' : 0,
				'1B' : 0,
				'2B' : 0,
				'3B' : 0,
				'HR' : 0,
				'H' : 0,
				'BInf' : 0,
				'GndO' : 0,
				'Bunt' : 0,
				'LinO' : 0,
				'PopO' : 0,
				'FC' : 0,
				'FlyO' : 0,
				'DP' : 0,
				'K' : 0,
				'TP' : 0,
				'CInf' : 0,
				'FInf' : 0,
				'E' : 0,
				'HBP' : 0,
				'IBB' : 0,
				'BB' : 0,
				'Sac' : 0,
				'AB_adj' : 0,
				'1B_adj' : 0,
				'2B_adj' : 0,
				'3B_adj' : 0,
				'HR_adj' : 0,
				'H_adj' : 0,
				'BInf_adj' : 0,
				'GndO_adj' : 0,
				'Bunt_adj' : 0,
				'LinO_adj' : 0,
				'PopO_adj' : 0,
				'FC_adj' : 0,
				'FlyO_adj' : 0,
				'DP_adj' : 0,
				'K_adj' : 0,
				'TP_adj' : 0,
				'CInf_adj' : 0,
				'FInf_adj' : 0,
				'E_adj' : 0,
				'HBP_adj' : 0,
				'IBB_adj' : 0,
				'BB_adj' : 0,
				'Sac_adj' : 0,
				'PA_adj' : 0,
				'OBP_adj' : 0,
				'SLG_adj' : 0,
				'OPS_adj' : 0,
				'1B_avg' : 0,
				'2B_avg' : 0,
				'3B_avg' : 0,
				'HR_avg' : 0,
				'H_avg' : 0,
				'BInf_avg' : 0,
				'GndO_avg' : 0,
				'Bunt_avg' : 0,
				'LinO_avg' : 0,
				'PopO_avg' : 0,
				'FlyO_avg' : 0,
				'DP_avg' : 0,
				'K_avg' : 0,
				'TP_avg' : 0,
				'CInf_avg' : 0,
				'FInf_avg' : 0,
				'E_avg' : 0,
				'HBP_avg' : 0,
				'IBB_avg' : 0,
				'BB_avg' : 0,
				'Sac_avg' : 0
				})
			db.pitcher_season.insert(
				{
				"playerID" : int(awayStarter),
				'stand' : 'R',
				'AB' : 0,
				'1B' : 0,
				'2B' : 0,
				'3B' : 0,
				'HR' : 0,
				'H' : 0,
				'BInf' : 0,
				'GndO' : 0,
				'Bunt' : 0,
				'LinO' : 0,
				'PopO' : 0,
				'FC' : 0,
				'FlyO' : 0,
				'DP' : 0,
				'K' : 0,
				'TP' : 0,
				'CInf' : 0,
				'FInf' : 0,
				'E' : 0,
				'HBP' : 0,
				'IBB' : 0,
				'BB' : 0,
				'Sac' : 0,
				'AB_adj' : 0,
				'1B_adj' : 0,
				'2B_adj' : 0,
				'3B_adj' : 0,
				'HR_adj' : 0,
				'H_adj' : 0,
				'BInf_adj' : 0,
				'GndO_adj' : 0,
				'Bunt_adj' : 0,
				'LinO_adj' : 0,
				'PopO_adj' : 0,
				'FC_adj' : 0,
				'FlyO_adj' : 0,
				'DP_adj' : 0,
				'K_adj' : 0,
				'TP_adj' : 0,
				'CInf_adj' : 0,
				'FInf_adj' : 0,
				'E_adj' : 0,
				'HBP_adj' : 0,
				'IBB_adj' : 0,
				'BB_adj' : 0,
				'Sac_adj' : 0,
				'PA_adj' : 0,
				'OBP_adj' : 0,
				'SLG_adj' : 0,
				'OPS_adj' : 0,
				'1B_avg' : 0,
				'2B_avg' : 0,
				'3B_avg' : 0,
				'HR_avg' : 0,
				'H_avg' : 0,
				'BInf_avg' : 0,
				'GndO_avg' : 0,
				'Bunt_avg' : 0,
				'LinO_avg' : 0,
				'PopO_avg' : 0,
				'FlyO_avg' : 0,
				'DP_avg' : 0,
				'K_avg' : 0,
				'TP_avg' : 0,
				'CInf_avg' : 0,
				'FInf_avg' : 0,
				'E_avg' : 0,
				'HBP_avg' : 0,
				'IBB_avg' : 0,
				'BB_avg' : 0,
				'Sac_avg' : 0
				})
		homeStarterLookup = db.pitcher_season.find_one({"playerID":int(homeStarter)})
		if(homeStarterLookup is None):
			print "insert blank"
			db.pitcher_season.insert(
				{
				"playerID" : int(homeStarter),
				'stand' : 'L',
				'AB' : 0,
				'1B' : 0,
				'2B' : 0,
				'3B' : 0,
				'HR' : 0,
				'H' : 0,
				'BInf' : 0,
				'GndO' : 0,
				'Bunt' : 0,
				'LinO' : 0,
				'PopO' : 0,
				'FC' : 0,
				'FlyO' : 0,
				'DP' : 0,
				'K' : 0,
				'TP' : 0,
				'CInf' : 0,
				'FInf' : 0,
				'E' : 0,
				'HBP' : 0,
				'IBB' : 0,
				'BB' : 0,
				'Sac' : 0,
				'AB_adj' : 0,
				'1B_adj' : 0,
				'2B_adj' : 0,
				'3B_adj' : 0,
				'HR_adj' : 0,
				'H_adj' : 0,
				'BInf_adj' : 0,
				'GndO_adj' : 0,
				'Bunt_adj' : 0,
				'LinO_adj' : 0,
				'PopO_adj' : 0,
				'FC_adj' : 0,
				'FlyO_adj' : 0,
				'DP_adj' : 0,
				'K_adj' : 0,
				'TP_adj' : 0,
				'CInf_adj' : 0,
				'FInf_adj' : 0,
				'E_adj' : 0,
				'HBP_adj' : 0,
				'IBB_adj' : 0,
				'BB_adj' : 0,
				'Sac_adj' : 0,
				'PA_adj' : 0,
				'OBP_adj' : 0,
				'SLG_adj' : 0,
				'OPS_adj' : 0,
				'1B_avg' : 0,
				'2B_avg' : 0,
				'3B_avg' : 0,
				'HR_avg' : 0,
				'H_avg' : 0,
				'BInf_avg' : 0,
				'GndO_avg' : 0,
				'Bunt_avg' : 0,
				'LinO_avg' : 0,
				'PopO_avg' : 0,
				'FlyO_avg' : 0,
				'DP_avg' : 0,
				'K_avg' : 0,
				'TP_avg' : 0,
				'CInf_avg' : 0,
				'FInf_avg' : 0,
				'E_avg' : 0,
				'HBP_avg' : 0,
				'IBB_avg' : 0,
				'BB_avg' : 0,
				'Sac_avg' : 0
				})
			db.pitcher_season.insert(
				{
				"playerID" : int(awayStarter),
				'stand' : 'R',
				'AB' : 0,
				'1B' : 0,
				'2B' : 0,
				'3B' : 0,
				'HR' : 0,
				'H' : 0,
				'BInf' : 0,
				'GndO' : 0,
				'Bunt' : 0,
				'LinO' : 0,
				'PopO' : 0,
				'FC' : 0,
				'FlyO' : 0,
				'DP' : 0,
				'K' : 0,
				'TP' : 0,
				'CInf' : 0,
				'FInf' : 0,
				'E' : 0,
				'HBP' : 0,
				'IBB' : 0,
				'BB' : 0,
				'Sac' : 0,
				'AB_adj' : 0,
				'1B_adj' : 0,
				'2B_adj' : 0,
				'3B_adj' : 0,
				'HR_adj' : 0,
				'H_adj' : 0,
				'BInf_adj' : 0,
				'GndO_adj' : 0,
				'Bunt_adj' : 0,
				'LinO_adj' : 0,
				'PopO_adj' : 0,
				'FC_adj' : 0,
				'FlyO_adj' : 0,
				'DP_adj' : 0,
				'K_adj' : 0,
				'TP_adj' : 0,
				'CInf_adj' : 0,
				'FInf_adj' : 0,
				'E_adj' : 0,
				'HBP_adj' : 0,
				'IBB_adj' : 0,
				'BB_adj' : 0,
				'Sac_adj' : 0,
				'PA_adj' : 0,
				'OBP_adj' : 0,
				'SLG_adj' : 0,
				'OPS_adj' : 0,
				'1B_avg' : 0,
				'2B_avg' : 0,
				'3B_avg' : 0,
				'HR_avg' : 0,
				'H_avg' : 0,
				'BInf_avg' : 0,
				'GndO_avg' : 0,
				'Bunt_avg' : 0,
				'LinO_avg' : 0,
				'PopO_avg' : 0,
				'FlyO_avg' : 0,
				'DP_avg' : 0,
				'K_avg' : 0,
				'TP_avg' : 0,
				'CInf_avg' : 0,
				'FInf_avg' : 0,
				'E_avg' : 0,
				'HBP_avg' : 0,
				'IBB_avg' : 0,
				'BB_avg' : 0,
				'Sac_avg' : 0
				})
		db.games_prog.update(
		{
			'gameID': gameID,
		},
		{
			'gameID': gameID,
			'date' : int(dateStr),
			'homeStarter': int(homeStarter),
			'awayStarter' : int(awayStarter)

		},
		upsert=True)
