import xml.etree.ElementTree as ET
import mongo_connect

def parseGameData(gameData,gameID,formattedDate):
	db = mongo_connect.connect()
	tree = ET.parse(gameData)
	root = tree.getroot()
	event_num = ""
	for inning in root.iter('inning'):
		inningNum = inning.attrib['num']
		for side in inning:
			inningSide = side.tag
			for atbat in side:
				if atbat.tag == "atbat": 
					num = atbat.attrib['num']
					print num
					b = atbat.attrib['b']
					s = atbat.attrib['s']
					o = atbat.attrib['o']
					start_tfs = atbat.attrib['start_tfs']
					start_tfs_zulu = atbat.attrib['start_tfs_zulu']
					batter = atbat.attrib['batter']
					stand = atbat.attrib['stand']
					pitcher = atbat.attrib['pitcher']
					p_throws = atbat.attrib['p_throws']
					des = atbat.attrib['des']
					if 'event_num' in atbat.attrib:
						event_num = atbat.attrib['event_num']
					else:
						event_num = ""
					event = atbat.attrib['event']
					if 'play_guid' in atbat.attrib:
						play_guid = atbat.attrib['play_guid']
					else:
						play_guid = ""
					home_team_runs = atbat.attrib['home_team_runs']
					away_team_runs = atbat.attrib['away_team_runs']
					print event_num
					result = db.batter_PA.update(
    				{
    					"gameday_link" : gameID,
    					"event_num": event_num
    				},
    				{
        				"playerID" : batter,
        				"pitcherID" : pitcher,
        				"inning" : inningNum,
        				"gamelink_num" : gameID,
        				"play_guid" : play_guid,
        				"date" : formattedDate,
        				"p_throws" : p_throws,
        				"event" : event,
        				"away_team_runs" : away_team_runs,
        				"event_num" : event_num,
        				"stand" : stand,
        				"start_tfs" : start_tfs,
        				"atbat_des" : des,
        				"inning_side" : inningSide,
        				"b" : b,
        				"home_team_runs" : home_team_runs,
        				"gameday_link" : gameID,
        				"o" : o,
        				"s" : s,
        				"start_tfs_zulu" : start_tfs_zulu
    				},
    				upsert=True)
    				result = db.pitcher_PA.update(
    				{
    					"gameday_link" : gameID,
    					"event_num": event_num
    				},
    				{
        				"playerID" : pitcher,
        				"batterID" : batter,
        				"inning" : inningNum,
        				"gamelink_num" : gameID,
        				"play_guid" : play_guid,
        				"date" : formattedDate,
        				"p_throws" : p_throws,
        				"event" : event,
        				"away_team_runs" : away_team_runs,
        				"event_num" : event_num,
        				"stand" : stand,
        				"start_tfs" : start_tfs,
        				"atbat_des" : des,
        				"inning_side" : inningSide,
        				"b" : b,
        				"home_team_runs" : home_team_runs,
        				"gameday_link" : gameID,
        				"o" : o,
        				"s" : s,
        				"start_tfs_zulu" : start_tfs_zulu
    				},
    				upsert=True)
	return "True"