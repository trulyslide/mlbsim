from datetime import date
import mongo_connect
import json
import urllib2

db = mongo_connect.connect()



today = date.today()
dateStr =  today.strftime("%Y%m%d")

year = dateStr[:4]
month = dateStr[4:6]
day = dateStr[-2:]
formattedDate = year + "_" + month + "_" + day
url = "http://gd2.mlb.com/components/game/mlb/year_" + year + "/month_" + month + "/day_" + day + "/miniscoreboard.json"
scoreboard = json.load(urllib2.urlopen(url))
games = scoreboard['data']['games']['game']
for game in games:
	homeBat = []
	homePit = []
	awayBat = []
	awayPit = []
	home_team = game['home_code']
	away_team= game['away_code']
	gameID = game['gameday_link']

	print gameID
	print home_team + " - " + away_team
	homeRoster = db.rosters.find( { "team": home_team })
	awayRoster = db.rosters.find( { "team": away_team })
	print homeRoster.count()
	print awayRoster.count()
	for player in homeRoster:
		print player
		#print player['name'] + " - " + player['pos']
		playerID = str(player['playerID'])
		#print playerID
		if (player['pos'] == 'bat'):
			stats = db.batter_season.find_one({ "playerID": playerID })
			if(stats != None):
				homeBat.append(stats)
		if (player['pos'] == 'pit'):
			stats = db.pitcher_season.find_one({ "playerID": playerID })
			if(stats != None):
				homePit.append(stats)
	for player in awayRoster:
		#print player['name'] + " - " + player['pos']
		playerID = str(player['playerID'])
		#print playerID
		if (player['pos'] == 'bat'):
			stats = db.batter_season.find_one({ "playerID": playerID })
			if(stats != None):
				awayBat.append(stats)
		if (player['pos'] == 'pit'):
			stats = db.pitcher_season.find_one({ "playerID": playerID })
			if(stats != None):
				awayPit.append(stats)

	for homeBatter in homeBat:
		homeBatterID = homeBatter['playerID']
		bat_1B_avg =  homeBatter['1B_avg']
		bat_2B_avg = homeBatter['2B_avg']
		bat_3B_avg = homeBatter['3B_avg']
		bat_HR_avg = homeBatter['HR_avg']
		bat_H_avg = homeBatter['H_avg']
		bat_BInf_avg = homeBatter['BInf_avg']
		bat_GndO_avg = homeBatter['GndO_avg']
		bat_Bunt_avg = homeBatter['Bunt_avg']
		bat_LinO_avg = homeBatter['LinO_avg']
		bat_PopO_avg = homeBatter['PopO_avg']
		bat_FlyO_avg = homeBatter['FlyO_avg']
		bat_DP_avg = homeBatter['DP_avg']
		bat_K_avg = homeBatter['K_avg']
		bat_TP_avg = homeBatter['TP_avg']
		bat_CInf_avg = homeBatter['CInf_avg']
		bat_FInf_avg = homeBatter['FInf_avg']
		bat_E_avg = homeBatter['E_avg']
		bat_HBP_avg = homeBatter['HBP_avg']
		bat_IBB_avg = homeBatter['IBB_avg']
		bat_BB_avg = homeBatter['BB_avg']
		bat_Sac_avg = homeBatter['Sac_avg']
		bat_OBP_adj = homeBatter['OBP_adj']
		bat_SLG_adj = homeBatter['SLG_adj']
		bat_OPS_adj = homeBatter['OPS_adj']
		for awayPitcher in awayPit:
			awayPitcherID = awayPitcher['playerID']
			pit_1B_avg =  awayPitcher['1B_avg']
			pit_2B_avg = awayPitcher['2B_avg']
			pit_3B_avg = awayPitcher['3B_avg']
			pit_HR_avg = awayPitcher['HR_avg']
			pit_H_avg = awayPitcher['H_avg']
			pit_BInf_avg = awayPitcher['BInf_avg']
			pit_GndO_avg = awayPitcher['GndO_avg']
			pit_Bunt_avg = awayPitcher['Bunt_avg']
			pit_LinO_avg = awayPitcher['LinO_avg']
			pit_PopO_avg = awayPitcher['PopO_avg']
			pit_FlyO_avg = awayPitcher['FlyO_avg']
			pit_DP_avg = awayPitcher['DP_avg']
			pit_K_avg = awayPitcher['K_avg']
			pit_TP_avg = awayPitcher['TP_avg']
			pit_CInf_avg = awayPitcher['CInf_avg']
			pit_FInf_avg = awayPitcher['FInf_avg']
			pit_E_avg = awayPitcher['E_avg']
			pit_HBP_avg = awayPitcher['HBP_avg']
			pit_IBB_avg = awayPitcher['IBB_avg']
			pit_BB_avg = awayPitcher['BB_avg']
			pit_Sac_avg = awayPitcher['Sac_avg']
			pit_OBP_adj = awayPitcher['OBP_adj']
			pit_SLG_adj = awayPitcher['SLG_adj']
			pit_OPS_adj = awayPitcher['OPS_adj']
			if(awayPitcher['AB'] != 0):
				tot_1B_avg =  (awayPitcher['1B_avg'] + homeBatter['1B_avg'])/2
				tot_2B_avg = (awayPitcher['2B_avg'] + homeBatter['2B_avg'])/2
				tot_3B_avg = (awayPitcher['3B_avg'] + homeBatter['3B_avg'])/2
				tot_HR_avg = (awayPitcher['HR_avg'] + homeBatter['HR_avg'])/2
				tot_H_avg = (awayPitcher['H_avg'] + homeBatter['H_avg'])/2
				tot_BInf_avg = (awayPitcher['BInf_avg'] + homeBatter['BInf_avg'])/2
				tot_GndO_avg = (awayPitcher['GndO_avg'] + homeBatter['GndO_avg'])/2
				tot_Bunt_avg = (awayPitcher['Bunt_avg'] + homeBatter['Bunt_avg'])/2
				tot_LinO_avg = (awayPitcher['LinO_avg'] + homeBatter['LinO_avg'])/2
				tot_PopO_avg = (awayPitcher['PopO_avg'] + homeBatter['PopO_avg'])/2
				tot_FlyO_avg = (awayPitcher['FlyO_avg'] + homeBatter['FlyO_avg'])/2
				tot_DP_avg = (awayPitcher['DP_avg'] + homeBatter['DP_avg'])/2
				tot_K_avg = (awayPitcher['K_avg'] + homeBatter['K_avg'])/2
				tot_TP_avg = (awayPitcher['TP_avg'] + homeBatter['TP_avg'])/2
				tot_CInf_avg = (awayPitcher['CInf_avg'] + homeBatter['CInf_avg'])/2
				tot_FInf_avg = (awayPitcher['FInf_avg'] + homeBatter['FInf_avg'])/2
				tot_E_avg = (awayPitcher['E_avg'] + homeBatter['E_avg'])/2
				tot_HBP_avg = (awayPitcher['HBP_avg'] +	 homeBatter['HBP_avg'])/2
				tot_IBB_avg = (awayPitcher['IBB_avg'] + homeBatter['IBB_avg'])/2
				tot_BB_avg = (awayPitcher['BB_avg'] + homeBatter['BB_avg'])/2
				tot_Sac_avg = (awayPitcher['Sac_avg'] + homeBatter['Sac_avg'])/2
				tot_OBP_adj = (pit_OBP_adj + bat_OBP_adj)/2
				tot_SLG_adj = (pit_SLG_adj + bat_SLG_adj)/2
				tot_OPS_adj = (pit_OPS_adj + bat_OPS_adj)/2
			else:
				tot_1B_avg =  homeBatter['1B_avg']
				tot_2B_avg = homeBatter['2B_avg']
				tot_3B_avg = homeBatter['3B_avg']
				tot_HR_avg = homeBatter['HR_avg']
				tot_H_avg = homeBatter['H_avg']
				tot_BInf_avg = homeBatter['BInf_avg']
				tot_GndO_avg = homeBatter['GndO_avg']
				tot_Bunt_avg = homeBatter['Bunt_avg']
				tot_LinO_avg = homeBatter['LinO_avg']
				tot_PopO_avg = homeBatter['PopO_avg']
				tot_FlyO_avg = homeBatter['FlyO_avg']
				tot_DP_avg = homeBatter['DP_avg']
				tot_K_avg = homeBatter['K_avg']
				tot_TP_avg = homeBatter['TP_avg']
				tot_CInf_avg = homeBatter['CInf_avg']
				tot_FInf_avg = homeBatter['FInf_avg']
				tot_E_avg = homeBatter['E_avg']
				tot_HBP_avg = homeBatter['HBP_avg']
				tot_IBB_avg = homeBatter['IBB_avg']
				tot_BB_avg = homeBatter['BB_avg']
				tot_Sac_avg = homeBatter['Sac_avg']
				tot_OBP_adj = bat_OBP_adj
				tot_SLG_adj = bat_SLG_adj
				tot_OPS_adj = bat_OPS_adj

				db.games.update(
				{
				'batterID': homeBatterID,
				'pitcherID' :awayPitcherID
				},
				{
				'batterID': homeBatterID,
				'pitcherID' :awayPitcherID,
				'1B_avg' : tot_1B_avg,
				'2B_avg' : tot_2B_avg,
				'3B_avg' : tot_3B_avg,
				'HR_avg' : tot_HR_avg,
				'H_avg' : tot_H_avg,
				'BInf_avg' : tot_BInf_avg,
				'GndO_avg' : tot_GndO_avg,
				'Bunt_avg' : tot_Bunt_avg,
			'LinO_avg' : tot_LinO_avg,
			'PopO_avg' : tot_PopO_avg,
			'FlyO_avg' : tot_FlyO_avg,
			'DP_avg' :tot_DP_avg,
			'K_avg' : tot_K_avg,
			'TP_avg' : tot_TP_avg,
			'CInf_avg' : tot_CInf_avg,
			'FInf_avg' : tot_FInf_avg,
			'E_avg' : tot_E_avg,
			'HBP_avg' : tot_HBP_avg,
			'IBB_avg' : tot_IBB_avg,
			'BB_avg' : tot_BB_avg,
			'Sac_avg' : tot_Sac_avg,
			'OBP_adj' : tot_OBP_adj,
			'SLG_adj' : tot_SLG_adj,
			'OPS_adj' : tot_OPS_adj
			},
			upsert=True)

	for awayBatter in awayBat:
		awayBatterID = awayBatter['playerID']
		bat_1B_avg =  awayBatter['1B_avg']
		bat_2B_avg = awayBatter['2B_avg']
		bat_3B_avg = awayBatter['3B_avg']
		bat_HR_avg = awayBatter['HR_avg']
		bat_H_avg = awayBatter['H_avg']
		bat_BInf_avg = awayBatter['BInf_avg']
		bat_GndO_avg = awayBatter['GndO_avg']
		bat_Bunt_avg = awayBatter['Bunt_avg']
		bat_LinO_avg = awayBatter['LinO_avg']
		bat_PopO_avg = awayBatter['PopO_avg']
		bat_FlyO_avg = awayBatter['FlyO_avg']
		bat_DP_avg = awayBatter['DP_avg']
		bat_K_avg = awayBatter['K_avg']
		bat_TP_avg = awayBatter['TP_avg']
		bat_CInf_avg = awayBatter['CInf_avg']
		bat_FInf_avg = awayBatter['FInf_avg']
		bat_E_avg = awayBatter['E_avg']
		bat_HBP_avg = awayBatter['HBP_avg']
		bat_IBB_avg = awayBatter['IBB_avg']
		bat_BB_avg = awayBatter['BB_avg']
		bat_Sac_avg = awayBatter['Sac_avg']
		bat_OBP_adj = awayBatter['OBP_adj']
		bat_SLG_adj = awayBatter['SLG_adj']
		bat_OPS_adj = awayBatter['OPS_adj']
		for homePitcher in homePit:
			homePitcherID = homePitcher['playerID']
			pit_1B_avg =  homePitcher['1B_avg']
			pit_2B_avg = homePitcher['2B_avg']
			pit_3B_avg = homePitcher['3B_avg']
			pit_HR_avg = homePitcher['HR_avg']
			pit_H_avg = homePitcher['H_avg']
			pit_BInf_avg = homePitcher['BInf_avg']
			pit_GndO_avg = homePitcher['GndO_avg']
			pit_Bunt_avg = homePitcher['Bunt_avg']
			pit_LinO_avg = homePitcher['LinO_avg']
			pit_PopO_avg = homePitcher['PopO_avg']
			pit_FlyO_avg = homePitcher['FlyO_avg']
			pit_DP_avg = homePitcher['DP_avg']
			pit_K_avg = homePitcher['K_avg']
			pit_TP_avg = homePitcher['TP_avg']
			pit_CInf_avg = homePitcher['CInf_avg']
			pit_FInf_avg = homePitcher['FInf_avg']
			pit_E_avg = homePitcher['E_avg']
			pit_HBP_avg = homePitcher['HBP_avg']
			pit_IBB_avg = homePitcher['IBB_avg']
			pit_BB_avg = homePitcher['BB_avg']
			pit_Sac_avg = homePitcher['Sac_avg']
			pit_OBP_adj = homePitcher['OBP_adj']
			pit_SLG_adj = homePitcher['SLG_adj']
			pit_OPS_adj = homePitcher['OPS_adj']

			if(homePitcher['AB'] != 0):
				tot_1B_avg =  (homePitcher['1B_avg'] + awayBatter['1B_avg'])/2
				tot_2B_avg = (homePitcher['2B_avg'] + awayBatter['2B_avg'])/2
				tot_3B_avg = (homePitcher['3B_avg'] + awayBatter['3B_avg'])/2
				tot_HR_avg = (homePitcher['HR_avg'] + awayBatter['HR_avg'])/2
				tot_H_avg = (homePitcher['H_avg'] + awayBatter['H_avg'])/2
				tot_BInf_avg = (homePitcher['BInf_avg'] + awayBatter['BInf_avg'])/2
				tot_GndO_avg = (homePitcher['GndO_avg'] + awayBatter['GndO_avg'])/2
				tot_Bunt_avg = (homePitcher['Bunt_avg'] + awayBatter['Bunt_avg'])/2
				tot_LinO_avg = (homePitcher['LinO_avg'] + awayBatter['LinO_avg'])/2
				tot_PopO_avg = (homePitcher['PopO_avg'] + awayBatter['PopO_avg'])/2
				tot_FlyO_avg = (homePitcher['FlyO_avg'] + awayBatter['FlyO_avg'])/2
				tot_DP_avg = (homePitcher['DP_avg'] + awayBatter['DP_avg'])/2
				tot_K_avg = (homePitcher['K_avg'] + awayBatter['K_avg'])/2
				tot_TP_avg = (homePitcher['TP_avg'] + awayBatter['TP_avg'])/2
				tot_CInf_avg = (homePitcher['CInf_avg'] + awayBatter['CInf_avg'])/2
				tot_FInf_avg = (homePitcher['FInf_avg'] + awayBatter['FInf_avg'])/2
				tot_E_avg = (homePitcher['E_avg'] + awayBatter['E_avg'])/2
				tot_HBP_avg = (homePitcher['HBP_avg'] + awayBatter['HBP_avg'])/2
				tot_IBB_avg = (homePitcher['IBB_avg'] + awayBatter['IBB_avg'])/2
				tot_BB_avg = (homePitcher['BB_avg'] + awayBatter['BB_avg'])/2
				tot_Sac_avg = (homePitcher['Sac_avg'] + awayBatter['Sac_avg'])/2
				tot_OBP_adj = (pit_OBP_adj + bat_OBP_adj)/2
				tot_SLG_adj = (pit_SLG_adj + bat_SLG_adj)/2
				tot_OPS_adj = (pit_OPS_adj + bat_OPS_adj)/2
			else:
				tot_1B_avg =  awayBatter['1B_avg']
				tot_2B_avg = awayBatter['2B_avg']
				tot_3B_avg = awayBatter['3B_avg']
				tot_HR_avg = awayBatter['HR_avg']
				tot_H_avg = awayBatter['H_avg']
				tot_BInf_avg = awayBatter['BInf_avg']
				tot_GndO_avg = awayBatter['GndO_avg']
				tot_Bunt_avg = awayBatter['Bunt_avg']
				tot_LinO_avg = awayBatter['LinO_avg']
				tot_PopO_avg = awayBatter['PopO_avg']
				tot_FlyO_avg = awayBatter['FlyO_avg']
				tot_DP_avg = awayBatter['DP_avg']
				tot_K_avg = awayBatter['K_avg']
				tot_TP_avg = awayBatter['TP_avg']
				tot_CInf_avg = awayBatter['CInf_avg']
				tot_FInf_avg = awayBatter['FInf_avg']
				tot_E_avg = awayBatter['E_avg']
				tot_HBP_avg = awayBatter['HBP_avg']
				tot_IBB_avg = awayBatter['IBB_avg']
				tot_BB_avg = awayBatter['BB_avg']
				tot_Sac_avg = awayBatter['Sac_avg']
				tot_OBP_adj = bat_OBP_adj
				tot_SLG_adj = bat_SLG_adj
				tot_OPS_adj = bat_OPS_adj
			db.games.update(
			{
			'batterID': awayBatterID,
			'pitcherID': homePitcherID
			},
			{
			'batterID': awayBatterID,
			'pitcherID': homePitcherID,
			'1B_avg' : tot_1B_avg,
			'2B_avg' : tot_2B_avg,
			'3B_avg' : tot_3B_avg,
			'HR_avg' : tot_HR_avg,
			'H_avg' : tot_H_avg,
			'BInf_avg' : tot_BInf_avg,
			'GndO_avg' : tot_GndO_avg,
			'Bunt_avg' : tot_Bunt_avg,
			'LinO_avg' : tot_LinO_avg,
			'PopO_avg' : tot_PopO_avg,
			'FlyO_avg' : tot_FlyO_avg,
			'DP_avg' :tot_DP_avg,
			'K_avg' : tot_K_avg,
			'TP_avg' : tot_TP_avg,
			'CInf_avg' : tot_CInf_avg,
			'FInf_avg' : tot_FInf_avg,
			'E_avg' : tot_E_avg,
			'HBP_avg' : tot_HBP_avg,
			'IBB_avg' : tot_IBB_avg,
			'BB_avg' : tot_BB_avg,
			'Sac_avg' : tot_Sac_avg,
			'OBP_adj' : tot_OBP_adj,
			'SLG_adj' : tot_SLG_adj,
			'OPS_adj' : tot_OPS_adj
			},
			upsert=True)

