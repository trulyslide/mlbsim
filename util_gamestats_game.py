import xml.etree.ElementTree as ET

def parseGameData(gameData,gameID):
	tree = ET.parse(gameData)
	root = tree.getroot()
	for inning in root.iter('inning'):
		inningNum = inning.atrib['num']
		for side in inning:
			inningSide = side.tag
			for atbat in side:
				if atbat.tag == "atbat": 
					num = atbat.atrib['num']
					b = atbat.atrib['b']
					s = atbat.atrib['s']
					o = atbat.atrib['o']
					start_tfs = atbat.atrib['start_tfs']
					start_tfs_zulu = atbat.atrib['start_tfs_zulu']
					batter = atbat.atrib['batter']
					stand = atbat.atrib['stand']
					pitcher = atbat.atrib['pitcher']
					p_throws = atbat.atrib['p_throws']
					des = atbat.atrib['des']
					event_num = atbat.atrib['event_num']
					event = atbat.atrib['event']
					play_guid = atbat.atrib['play_guid']
					home_team_runs = atbat.atrib['home_team_runs']
					away_team_runs = atbat.atrib['away_team_runs']

					result = dbMongo.batter_PA.insert_one(
    				{
        				"playerID" : batter,
        				"pitcherID" : pitcher,
        				"inning" : inningNum,
        				"gamelink_num" : gameID,
        				"play_guid" : play_guid,
        				"date" : xxx,
        				"p_throws" : xxx,
        				"event" : xxx,
        				"score" : xxx,
        				"away_team_runs" : xxx,
        				"event_num" : xxx,
        				"stand" : xxx,
        				"start_tfs" : xxx,
        				"atbat_des" : xxx,
        				"inning_side" : inningSide,
        				"b" : xxx,
        				"home_team_runs" : xxx,
        				"gameday_link" : xxx,
        				"o" : xxx,
        				"s" : xxx,
        				"start_tfs_zulu" : xxx
    				})
	return "True"