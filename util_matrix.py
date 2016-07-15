from datetime import date
import mongo_connect
import json
import urllib2

db = mongo_connect.connect()


db.games.remove({})
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
	homeBat = []
	homePit = []
	awayBat = []
	awayPit = []
	home_team = game['home_code']
	away_team= game['away_code']
	gameID = game['gameday_link']
	factors_L = db.factors.find_one({"team": home_team, "stand": "L"})
    	facHR_L = factors_L['HR']
    	fac1B_L = factors_L['1B']
    	fac2B_L = factors_L['2B']
    	fac3B_L = factors_L['3B']
    	factors_R = db.factors.find_one({"team": home_team, "stand": "R"})
    	facHR_R = factors_R['HR']
    	fac1B_R = factors_R['1B']
    	fac2B_R = factors_R['2B']
    	fac3B_R = factors_R['3B']

	print gameID
	print home_team + " - " + away_team
	homeRoster = db.rosters.find( { "team": home_team })
	awayRoster = db.rosters.find( { "team": away_team })

	for player in homeRoster:
		if (player['pos'] == 'bat'):
			homeBat.append(player)
		if (player['pos'] == 'pit'):
			homePit.append(player)
	for player in awayRoster:
		if (player['pos'] == 'bat'):
			awayBat.append(player)
		if (player['pos'] == 'pit'):
			awayPit.append(player)

	for homeBatter in homeBat:
		homeBatterID =homeBatter['playerID']
		homeBatterStand = homeBatter['bats']

		for awayPitcher in awayPit:
			awayPitcherID = awayPitcher['playerID']
			awayPitcherThrows = awayPitcher['throws']
			if(homeBatterStand == "S"):
				if(awayPitcherThrows == "L"):
					homeBatterStand = "R"
				if(awayPitcherThrows == "R"):
					homeBatterStand = "L"
			batterStats = db.batter_season.find_one({"playerID": homeBatterID, "throws": awayPitcherThrows})
			pitcherStats = db.pitcher_season.find_one({"playerID": awayPitcherID, "stand": homeBatterStand})

			if (batterStats is not None):
				bat_1B_avg =  batterStats['1B_avg']
				bat_2B_avg = batterStats['2B_avg']
				bat_3B_avg = batterStats['3B_avg']
				bat_HR_avg = batterStats['HR_avg']
				bat_H_avg = batterStats['H_avg']
				bat_BInf_avg = batterStats['BInf_avg']
				bat_GndO_avg = batterStats['GndO_avg']
				bat_Bunt_avg = batterStats['Bunt_avg']
				bat_LinO_avg = batterStats['LinO_avg']
				bat_PopO_avg = batterStats['PopO_avg']
				bat_FlyO_avg = batterStats['FlyO_avg']
				bat_DP_avg = batterStats['DP_avg']
				bat_K_avg = batterStats['K_avg']
				bat_TP_avg = batterStats['TP_avg']
				bat_CInf_avg = batterStats['CInf_avg']
				bat_FInf_avg = batterStats['FInf_avg']
				bat_E_avg = batterStats['E_avg']
				bat_HBP_avg = batterStats['HBP_avg']
				bat_IBB_avg = batterStats['IBB_avg']
				bat_BB_avg = batterStats['BB_avg']
				bat_Sac_avg = batterStats['Sac_avg']
				bat_OBP_adj = batterStats['OBP_adj']
				bat_SLG_adj = batterStats['SLG_adj']
				bat_OPS_adj = batterStats['OPS_adj']
				if(pitcherStats is not None):
					pit_1B_avg =  pitcherStats['1B_avg']
					pit_2B_avg = pitcherStats['2B_avg']
					pit_3B_avg = pitcherStats['3B_avg']
					pit_HR_avg = pitcherStats['HR_avg']
					pit_H_avg = pitcherStats['H_avg']
				else:
					pit_1B_avg =  batterStats['1B_avg']
					pit_2B_avg = batterStats['2B_avg']
					pit_3B_avg = batterStats['3B_avg']
					pit_HR_avg = batterStats['HR_avg']
					pit_H_avg = batterStats['H_avg']
				if(homeBatterStand == 'L'):
					bat_1B_avg = bat_1B_avg * fac1B_L
					bat_2B_avg = bat_2B_avg * fac2B_L
					bat_3B_avg = bat_3B_avg * fac3B_L
					bat_HR_avg = bat_HR_avg * facHR_L
					pit_1B_avg = pit_1B_avg * fac1B_L
					pit_2B_avg = pit_2B_avg * fac2B_L
					pit_3B_avg = pit_3B_avg * fac3B_L
					pit_HR_avg = pit_HR_avg * facHR_L
				if(homeBatterStand == 'R'):
					bat_1B_avg = bat_1B_avg * fac1B_R
					bat_2B_avg = bat_2B_avg * fac2B_R
					bat_3B_avg = bat_3B_avg * fac3B_R
					bat_HR_avg = bat_HR_avg * facHR_R
					pit_1B_avg = pit_1B_avg * fac1B_R
					pit_2B_avg = pit_2B_avg * fac2B_R
					pit_3B_avg = pit_3B_avg * fac3B_R
					pit_HR_avg = pit_HR_avg * facHR_R
				if(homeBatterStand == 'S' and awayPitcher['throws'] == 'L'):
					bat_1B_avg = bat_1B_avg * fac1B_R
					bat_2B_avg = bat_2B_avg * fac2B_R
					bat_3B_avg = bat_3B_avg * fac3B_R
					bat_HR_avg = bat_HR_avg * facHR_R
					pit_1B_avg = pit_1B_avg * fac1B_R
					pit_2B_avg = pit_2B_avg * fac2B_R
					pit_3B_avg = pit_3B_avg * fac3B_R
					pit_HR_avg = pit_HR_avg * facHR_R
				if(homeBatterStand == 'S' and awayPitcher['throws'] == 'R'):
					bat_1B_avg = bat_1B_avg * fac1B_L
					bat_2B_avg = bat_2B_avg * fac2B_L
					bat_3B_avg = bat_3B_avg * fac3B_L
					bat_HR_avg = bat_HR_avg * facHR_L
					pit_1B_avg = pit_1B_avg * fac1B_L
					pit_2B_avg = pit_2B_avg * fac2B_L
					pit_3B_avg = pit_3B_avg * fac3B_L
					pit_HR_avg = pit_HR_avg * facHR_L
				if(pitcherStats is not None):
					pit_BInf_avg = pitcherStats['BInf_avg']
					pit_GndO_avg = pitcherStats['GndO_avg']
					pit_Bunt_avg = pitcherStats['Bunt_avg']
					pit_LinO_avg = pitcherStats['LinO_avg']
					pit_PopO_avg = pitcherStats['PopO_avg']
					pit_FlyO_avg = pitcherStats['FlyO_avg']
					pit_DP_avg = pitcherStats['DP_avg']
					pit_K_avg = pitcherStats['K_avg']
					pit_TP_avg = pitcherStats['TP_avg']
					pit_CInf_avg = pitcherStats['CInf_avg']
					pit_FInf_avg = pitcherStats['FInf_avg']
					pit_E_avg = pitcherStats['E_avg']
					pit_HBP_avg = pitcherStats['HBP_avg']
					pit_IBB_avg = pitcherStats['IBB_avg']
					pit_BB_avg = pitcherStats['BB_avg']
					pit_Sac_avg = pitcherStats['Sac_avg']
					pit_OBP_adj = pitcherStats['OBP_adj']
					pit_SLG_adj = pitcherStats['SLG_adj']
					pit_OPS_adj = pitcherStats['OPS_adj']
				else:
					pit_BInf_avg = batterStats['BInf_avg']
					pit_GndO_avg = batterStats['GndO_avg']
					pit_Bunt_avg = batterStats['Bunt_avg']
					pit_LinO_avg = batterStats['LinO_avg']
					pit_PopO_avg = batterStats['PopO_avg']
					pit_FlyO_avg = batterStats['FlyO_avg']
					pit_DP_avg = batterStats['DP_avg']
					pit_K_avg = batterStats['K_avg']
					pit_TP_avg = batterStats['TP_avg']
					pit_CInf_avg = batterStats['CInf_avg']
					pit_FInf_avg = batterStats['FInf_avg']
					pit_E_avg = batterStats['E_avg']
					pit_HBP_avg = batterStats['HBP_avg']
					pit_IBB_avg = batterStats['IBB_avg']
					pit_BB_avg = batterStats['BB_avg']
					pit_Sac_avg = batterStats['Sac_avg']
					pit_OBP_adj = batterStats['OBP_adj']
					pit_SLG_adj = batterStats['SLG_adj']
					pit_OPS_adj = batterStats['OPS_adj']
				if(pitcherStats is not None):
					tot_1B_avg =  (pitcherStats['1B_avg'] + batterStats['1B_avg'])/2
					tot_2B_avg = (pitcherStats['2B_avg'] + batterStats['2B_avg'])/2
					tot_3B_avg = (pitcherStats['3B_avg'] + batterStats['3B_avg'])/2
					tot_HR_avg = (pitcherStats['HR_avg'] + batterStats['HR_avg'])/2
					tot_H_avg = (pitcherStats['H_avg'] + batterStats['H_avg'])/2
					tot_BInf_avg = (pitcherStats['BInf_avg'] + batterStats['BInf_avg'])/2
					tot_GndO_avg = (pitcherStats['GndO_avg'] + batterStats['GndO_avg'])/2
					tot_Bunt_avg = (pitcherStats['Bunt_avg'] + batterStats['Bunt_avg'])/2
					tot_LinO_avg = (pitcherStats['LinO_avg'] + batterStats['LinO_avg'])/2
					tot_PopO_avg = (pitcherStats['PopO_avg'] + batterStats['PopO_avg'])/2
					tot_FlyO_avg = (pitcherStats['FlyO_avg'] + batterStats['FlyO_avg'])/2
					tot_DP_avg = (pitcherStats['DP_avg'] + batterStats['DP_avg'])/2
					tot_K_avg = (pitcherStats['K_avg'] + batterStats['K_avg'])/2
					tot_TP_avg = (pitcherStats['TP_avg'] + batterStats['TP_avg'])/2
					tot_CInf_avg = (pitcherStats['CInf_avg'] + batterStats['CInf_avg'])/2
					tot_FInf_avg = (pitcherStats['FInf_avg'] + batterStats['FInf_avg'])/2
					tot_E_avg = (pitcherStats['E_avg'] + batterStats['E_avg'])/2
					tot_HBP_avg = (pitcherStats['HBP_avg'] +	 batterStats['HBP_avg'])/2
					tot_IBB_avg = (pitcherStats['IBB_avg'] + batterStats['IBB_avg'])/2
					tot_BB_avg = (pitcherStats['BB_avg'] + batterStats['BB_avg'])/2
					tot_Sac_avg = (pitcherStats['Sac_avg'] + batterStats['Sac_avg'])/2
					tot_AB_avg = 1 - tot_CInf_avg - tot_FInf_avg - tot_E_avg - tot_HBP_avg - tot_BB_avg
					tot_OBP_adj = tot_H_avg + tot_CInf_avg + tot_FInf_avg + tot_E_avg + tot_HBP_avg + tot_HBP_avg
					tot_wOBA_adj = (tot_1B_avg*0.879 + tot_2B_avg*1.241 + tot_3B_avg*1.567 + tot_HR_avg*2.01 + tot_BB_avg*0.691 + tot_HBP_avg*0.722)/(1 - tot_Sac_avg - tot_HBP_avg - tot_IBB_avg)
					tot_SLG_adj = (tot_1B_avg + tot_2B_avg*2 + tot_3B_avg*3 + tot_HR_avg*4)/tot_AB_avg
					tot_OPS_adj = tot_OBP_adj + tot_SLG_adj
				else:
					tot_1B_avg =  batterStats['1B_avg']
					tot_2B_avg = batterStats['2B_avg']
					tot_3B_avg = batterStats['3B_avg']
					tot_HR_avg = batterStats['HR_avg']
					tot_H_avg = batterStats['H_avg']
					tot_BInf_avg = batterStats['BInf_avg']
					tot_GndO_avg = batterStats['GndO_avg']
					tot_Bunt_avg = batterStats['Bunt_avg']
					tot_LinO_avg = batterStats['LinO_avg']
					tot_PopO_avg = batterStats['PopO_avg']
					tot_FlyO_avg = batterStats['FlyO_avg']
					tot_DP_avg = batterStats['DP_avg']
					tot_K_avg = batterStats['K_avg']
					tot_TP_avg = batterStats['TP_avg']
					tot_CInf_avg = batterStats['CInf_avg']
					tot_FInf_avg = batterStats['FInf_avg']
					tot_E_avg = batterStats['E_avg']
					tot_HBP_avg = batterStats['HBP_avg']
					tot_IBB_avg = batterStats['IBB_avg']
					tot_BB_avg = batterStats['BB_avg']
					tot_Sac_avg = batterStats['Sac_avg']
					tot_AB_avg = 1 - tot_CInf_avg - tot_FInf_avg - tot_E_avg - tot_HBP_avg - tot_BB_avg
					tot_OBP_adj = tot_H_avg + tot_CInf_avg + tot_FInf_avg + tot_E_avg + tot_HBP_avg + tot_HBP_avg
					if(tot_AB_avg != 0):
						tot_SLG_adj = (tot_1B_avg + tot_2B_avg*2 + tot_3B_avg*3 + tot_HR_avg*4)/tot_AB_avg
						tot_wOBA_adj = (tot_1B_avg*0.879 + tot_2B_avg*1.241 + tot_3B_avg*1.567 + tot_HR_avg*2.01 + tot_BB_avg*0.691 + tot_HBP_avg*0.722)/(1 - tot_Sac_avg - tot_HBP_avg - tot_IBB_avg)
					else:
						tot_SLG_adj = 0
						tot_wOBA = 0
					tot_OPS_adj = tot_OBP_adj + tot_SLG_adj

				db.games.insert(
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
				'OPS_adj' : tot_OPS_adj,
				'wOBA_adj' : tot_wOBA_adj
				})

	for awayBatter in awayBat:
		awayBatterID = awayBatter['playerID']
		awayBatterStand = awayBatter['bats']

		for homePitcher in homePit:
			homePitcherID = homePitcher['playerID']
			homePitcherThrows = homePitcher['throws']
			if(awayBatterStand == "S"):
				if(homePitcherThrows == "L"):
					awayBatterStand = "R"
				if(homePitcherThrows == "R"):
					awayBatterStand = "L"
			batterStats = db.batter_season.find_one({"playerID": awayBatterID, "throws": homePitcherThrows})
			pitcherStats = db.pitcher_season.find_one({"playerID": homePitcherID, "stand": awayBatterStand})
			if (batterStats is not None):
				bat_1B_avg =  batterStats['1B_avg']
				bat_2B_avg = batterStats['2B_avg']
				bat_3B_avg = batterStats['3B_avg']
				bat_HR_avg = batterStats['HR_avg']
				bat_H_avg = batterStats['H_avg']
				bat_BInf_avg = batterStats['BInf_avg']
				bat_GndO_avg = batterStats['GndO_avg']
				bat_Bunt_avg = batterStats['Bunt_avg']
				bat_LinO_avg = batterStats['LinO_avg']
				bat_PopO_avg = batterStats['PopO_avg']
				bat_FlyO_avg = batterStats['FlyO_avg']
				bat_DP_avg = batterStats['DP_avg']
				bat_K_avg = batterStats['K_avg']
				bat_TP_avg = batterStats['TP_avg']
				bat_CInf_avg = batterStats['CInf_avg']
				bat_FInf_avg = batterStats['FInf_avg']
				bat_E_avg = batterStats['E_avg']
				bat_HBP_avg = batterStats['HBP_avg']
				bat_IBB_avg = batterStats['IBB_avg']
				bat_BB_avg = batterStats['BB_avg']
				bat_Sac_avg = batterStats['Sac_avg']
				bat_OBP_adj = batterStats['OBP_adj']
				bat_SLG_adj = batterStats['SLG_adj']
				bat_OPS_adj = batterStats['OPS_adj']

				if(pitcherStats is not None):
					pit_1B_avg =  pitcherStats['1B_avg']
					pit_2B_avg = pitcherStats['2B_avg']
					pit_3B_avg = pitcherStats['3B_avg']
					pit_HR_avg = pitcherStats['HR_avg']
					pit_H_avg = pitcherStats['H_avg']
				else:
					pit_1B_avg =  batterStats['1B_avg']
					pit_2B_avg = batterStats['2B_avg']
					pit_3B_avg = batterStats['3B_avg']
					pit_HR_avg = batterStats['HR_avg']
					pit_H_avg = batterStats['H_avg']
				if(homeBatterStand == 'L'):
					bat_1B_avg = bat_1B_avg * fac1B_L
					bat_2B_avg = bat_2B_avg * fac2B_L
					bat_3B_avg = bat_3B_avg * fac3B_L
					bat_HR_avg = bat_HR_avg * facHR_L
					pit_1B_avg = pit_1B_avg * fac1B_L
					pit_2B_avg = pit_2B_avg * fac2B_L
					pit_3B_avg = pit_3B_avg * fac3B_L
					pit_HR_avg = pit_HR_avg * facHR_L
				if(homeBatterStand == 'R'):
					bat_1B_avg = bat_1B_avg * fac1B_R
					bat_2B_avg = bat_2B_avg * fac2B_R
					bat_3B_avg = bat_3B_avg * fac3B_R
					bat_HR_avg = bat_HR_avg * facHR_R
					pit_1B_avg = pit_1B_avg * fac1B_R
					pit_2B_avg = pit_2B_avg * fac2B_R
					pit_3B_avg = pit_3B_avg * fac3B_R
					pit_HR_avg = pit_HR_avg * facHR_R
				if(homeBatterStand == 'S' and awayPitcher['throws'] == 'L'):
					bat_1B_avg = bat_1B_avg * fac1B_R
					bat_2B_avg = bat_2B_avg * fac2B_R
					bat_3B_avg = bat_3B_avg * fac3B_R
					bat_HR_avg = bat_HR_avg * facHR_R
					pit_1B_avg = pit_1B_avg * fac1B_R
					pit_2B_avg = pit_2B_avg * fac2B_R
					pit_3B_avg = pit_3B_avg * fac3B_R
					pit_HR_avg = pit_HR_avg * facHR_R
				if(homeBatterStand == 'S' and awayPitcher['throws'] == 'R'):
					bat_1B_avg = bat_1B_avg * fac1B_L
					bat_2B_avg = bat_2B_avg * fac2B_L
					bat_3B_avg = bat_3B_avg * fac3B_L
					bat_HR_avg = bat_HR_avg * facHR_L
					pit_1B_avg = pit_1B_avg * fac1B_L
					pit_2B_avg = pit_2B_avg * fac2B_L
					pit_3B_avg = pit_3B_avg * fac3B_L
					pit_HR_avg = pit_HR_avg * facHR_L
				if(pitcherStats is not None):
					pit_BInf_avg = pitcherStats['BInf_avg']
					pit_GndO_avg = pitcherStats['GndO_avg']
					pit_Bunt_avg = pitcherStats['Bunt_avg']
					pit_LinO_avg = pitcherStats['LinO_avg']
					pit_PopO_avg = pitcherStats['PopO_avg']
					pit_FlyO_avg = pitcherStats['FlyO_avg']
					pit_DP_avg = pitcherStats['DP_avg']
					pit_K_avg = pitcherStats['K_avg']
					pit_TP_avg = pitcherStats['TP_avg']
					pit_CInf_avg = pitcherStats['CInf_avg']
					pit_FInf_avg = pitcherStats['FInf_avg']
					pit_E_avg = pitcherStats['E_avg']
					pit_HBP_avg = pitcherStats['HBP_avg']
					pit_IBB_avg = pitcherStats['IBB_avg']
					pit_BB_avg = pitcherStats['BB_avg']
					pit_Sac_avg = pitcherStats['Sac_avg']
					pit_OBP_adj = pitcherStats['OBP_adj']
					pit_SLG_adj = pitcherStats['SLG_adj']
					pit_OPS_adj = pitcherStats['OPS_adj']
				else:
					pit_BInf_avg = batterStats['BInf_avg']
					pit_GndO_avg = batterStats['GndO_avg']
					pit_Bunt_avg = batterStats['Bunt_avg']
					pit_LinO_avg = batterStats['LinO_avg']
					pit_PopO_avg = batterStats['PopO_avg']
					pit_FlyO_avg = batterStats['FlyO_avg']
					pit_DP_avg = batterStats['DP_avg']
					pit_K_avg = batterStats['K_avg']
					pit_TP_avg = batterStats['TP_avg']
					pit_CInf_avg = batterStats['CInf_avg']
					pit_FInf_avg = batterStats['FInf_avg']
					pit_E_avg = batterStats['E_avg']
					pit_HBP_avg = batterStats['HBP_avg']
					pit_IBB_avg = batterStats['IBB_avg']
					pit_BB_avg = batterStats['BB_avg']
					pit_Sac_avg = batterStats['Sac_avg']
					pit_OBP_adj = batterStats['OBP_adj']
					pit_SLG_adj = batterStats['SLG_adj']
					pit_OPS_adj = batterStats['OPS_adj']
				if(pitcherStats is not None):
					tot_1B_avg =  (pitcherStats['1B_avg'] + batterStats['1B_avg'])/2
					tot_2B_avg = (pitcherStats['2B_avg'] + batterStats['2B_avg'])/2
					tot_3B_avg = (pitcherStats['3B_avg'] + batterStats['3B_avg'])/2
					tot_HR_avg = (pitcherStats['HR_avg'] + batterStats['HR_avg'])/2
					tot_H_avg = (pitcherStats['H_avg'] + batterStats['H_avg'])/2
					tot_BInf_avg = (pitcherStats['BInf_avg'] + batterStats['BInf_avg'])/2
					tot_GndO_avg = (pitcherStats['GndO_avg'] + batterStats['GndO_avg'])/2
					tot_Bunt_avg = (pitcherStats['Bunt_avg'] + batterStats['Bunt_avg'])/2
					tot_LinO_avg = (pitcherStats['LinO_avg'] + batterStats['LinO_avg'])/2
					tot_PopO_avg = (pitcherStats['PopO_avg'] + batterStats['PopO_avg'])/2
					tot_FlyO_avg = (pitcherStats['FlyO_avg'] + batterStats['FlyO_avg'])/2
					tot_DP_avg = (pitcherStats['DP_avg'] + batterStats['DP_avg'])/2
					tot_K_avg = (pitcherStats['K_avg'] + batterStats['K_avg'])/2
					tot_TP_avg = (pitcherStats['TP_avg'] + batterStats['TP_avg'])/2
					tot_CInf_avg = (pitcherStats['CInf_avg'] + batterStats['CInf_avg'])/2
					tot_FInf_avg = (pitcherStats['FInf_avg'] + batterStats['FInf_avg'])/2
					tot_E_avg = (pitcherStats['E_avg'] + batterStats['E_avg'])/2
					tot_HBP_avg = (pitcherStats['HBP_avg'] +	 batterStats['HBP_avg'])/2
					tot_IBB_avg = (pitcherStats['IBB_avg'] + batterStats['IBB_avg'])/2
					tot_BB_avg = (pitcherStats['BB_avg'] + batterStats['BB_avg'])/2
					tot_Sac_avg = (pitcherStats['Sac_avg'] + batterStats['Sac_avg'])/2
					tot_AB_avg = 1 - tot_CInf_avg - tot_FInf_avg - tot_E_avg - tot_HBP_avg - tot_BB_avg
					tot_wOBA_adj = (tot_1B_avg*0.879 + tot_2B_avg*1.241 + tot_3B_avg*1.567 + tot_HR_avg*2.01 + tot_BB_avg*0.691 + tot_HBP_avg*0.722)/(1 - tot_Sac_avg - tot_HBP_avg - tot_IBB_avg)
					tot_OBP_adj = tot_H_avg + tot_CInf_avg + tot_FInf_avg + tot_E_avg + tot_HBP_avg + tot_HBP_avg
					tot_SLG_adj = (tot_1B_avg + tot_2B_avg*2 + tot_3B_avg*3 + tot_HR_avg*4)/tot_AB_avg
					tot_OPS_adj = tot_OBP_adj + tot_SLG_adj
				else:
					tot_1B_avg =  batterStats['1B_avg']
					tot_2B_avg = batterStats['2B_avg']
					tot_3B_avg = batterStats['3B_avg']
					tot_HR_avg = batterStats['HR_avg']
					tot_H_avg = batterStats['H_avg']
					tot_BInf_avg = batterStats['BInf_avg']
					tot_GndO_avg = batterStats['GndO_avg']
					tot_Bunt_avg = batterStats['Bunt_avg']
					tot_LinO_avg = batterStats['LinO_avg']
					tot_PopO_avg = batterStats['PopO_avg']
					tot_FlyO_avg = batterStats['FlyO_avg']
					tot_DP_avg = batterStats['DP_avg']
					tot_K_avg = batterStats['K_avg']
					tot_TP_avg = batterStats['TP_avg']
					tot_CInf_avg = batterStats['CInf_avg']
					tot_FInf_avg = batterStats['FInf_avg']
					tot_E_avg = batterStats['E_avg']
					tot_HBP_avg = batterStats['HBP_avg']
					tot_IBB_avg = batterStats['IBB_avg']
					tot_BB_avg = batterStats['BB_avg']
					tot_Sac_avg = batterStats['Sac_avg']
					tot_AB_avg = 1 - tot_CInf_avg - tot_FInf_avg - tot_E_avg - tot_HBP_avg - tot_BB_avg
					tot_OBP_adj = tot_H_avg + tot_CInf_avg + tot_FInf_avg + tot_E_avg + tot_HBP_avg + tot_HBP_avg
					if(tot_AB_avg != 0):
						tot_SLG_adj = (tot_1B_avg + tot_2B_avg*2 + tot_3B_avg*3 + tot_HR_avg*4)/tot_AB_avg
						tot_wOBA_adj = (tot_1B_avg*0.879 + tot_2B_avg*1.241 + tot_3B_avg*1.567 + tot_HR_avg*2.01 + tot_BB_avg*0.691 + tot_HBP_avg*0.722)/(1 - tot_Sac_avg - tot_HBP_avg - tot_IBB_avg)
					else:
						tot_SLG_adj = 0
						tot_wOBA_adj = 0
					tot_OPS_adj = tot_OBP_adj + tot_SLG_adj

				db.games.insert(
				{
				'batterID': awayBatterID,
				'pitcherID' :homePitcherID,
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
				'OPS_adj' : tot_OPS_adj,
				'wOBA_adj' : tot_wOBA_adj
				})
