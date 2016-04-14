import MySQLdb
from pymongo import MongoClient

client = MongoClient()
dbMongo = client.mlb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="mlb",         # your username
                     passwd="mlb",  # your password
                     db="mlb")        # name of the data base

cur = db.cursor()
cur.execute("SELECT * FROM gd_atbat2015")
i=1
for row in cur.fetchall():
    if(i > 0):
	    pitcherID =  int(row[1])
	    batterID = int(row[2])
	    num = int(row[3])
	    b = int(row[4])
	    s = int(row[5])
	    o = int(row[6])
	    start_tfs = str(row[7])
	    start_tfs_zulu = str(row[8])
	    stand = str(row[9])
	    b_height = str(row[10])
	    p_throws = str(row[11])
	    atbat_des = str(row[12])
	    event = str(row[14])
	    score = str(row[15])
	    home_team_runs = int(row[16])
	    away_team_runs = int(row[17])
	    url = str(row[18])
	    inning_side = str(row[19])
	    inning = int(row[20])
	    next_ = str(row[21])
	    event2 = str(row[22])
	    event3 = str(row[23])
	    batter_name = str(row[24])
	    pitcher_name = str(row[25])
	    event4 = str(row[26])
	    gameday_link = str(row[27])
	    date = str(row[28])
	    event_num = int(row[29])
	    play_guid = str(row[34])
	   
	    result = dbMongo.batter_PA.insert_one(
	        {
	            'playerID': batterID,
	            'gamelink_num': gameday_link + str(num),
	            'pitcherID': pitcherID,
	            'num': num,
	            'b': b,
	            's': s,
	            'o': o,
	            'start_tfs': start_tfs,
	            'start_tfs_zulu': start_tfs_zulu,
	            'stand': stand,
	            'b_height': b_height,
	            'p_throws': p_throws,
	            'atbat_des': atbat_des,
	            'event': event,
	            'score': score,
	            'home_team_runs': home_team_runs,
	            'away_team_runs': away_team_runs,
	            'url': url,
	            'inning_side': inning_side,
	            'inning': inning,
	            'next_': next_,
	            'event2': event2,
	            'event3': event3,
	            'batter_name': batter_name,
	            'pitcher_name': pitcher_name,
	            'event4': event4,
	            'gameday_link': gameday_link,
	            'date': date,
	            'event_num': event_num,
	            'play_guid': play_guid
	        }
	    )
	    result = dbMongo.pitcher_PA.insert_one(
	        {
	            'playerID': pitcherID,
	            'gamelink_num': gameday_link + str(num),
	            'batterID': batterID,
	            'num': num,
	            'b': b,
	            's': s,
	            'o': o,
	            'start_tfs': start_tfs,
	            'start_tfs_zulu': start_tfs_zulu,
	            'stand': stand,
	            'b_height': b_height,
	            'p_throws': p_throws,
	            'atbat_des': atbat_des,
	            'event': event,
	            'score': score,
	            'home_team_runs': home_team_runs,
	            'away_team_runs': away_team_runs,
	            'url': url,
	            'inning_side': inning_side,
	            'inning': inning,
	            'next_': next_,
	            'event2': event2,
	            'event3': event3,
	            'batter_name': batter_name,
	            'pitcher_name': pitcher_name,
	            'event4': event4,
	            'gameday_link': gameday_link,
	            'date': date,
	            'event_num': event_num,
	            'play_guid': play_guid
	        }
	    )
    print i
    i+=1
db.close()