import mongo_connect
import datetime
from datetime import date

def player_daily_adjust():
	db = mongo_connect.connect()

	today = int(date.today().strftime('%Y%m%d'))
	print today

	gameDates = db.game_dates.find( { "date": {"$lt": today }} ).sort([("date", -1)]).limit(100)

	adj = 100
	for gameDate in gameDates:
		gdate =  gameDate['date']
		print gdate
		batterDailys = db.batter_PA_daily.find( { "date": gdate} )
		pitcherDailys = db.pitcher_PA_daily.find( { "date": gdate} )
		print batterDailys.count()
		print pitcherDailys.count()
		for batter in batterDailys:
			playerID = batter['playerID']
			adj_1B = batter['1Bfac'] * adj
			adj_2B = batter['2Bfac'] * adj
			adj_3B = batter['3Bfac'] * adj
			adj_HR = batter['HRfac'] * adj
			adj_H = batter['Hfac'] * adj
			adj_BInf = batter['BInf'] * adj
			adj_GndO = batter['GndO'] * adj
			adj_Bunt = batter['Bunt'] * adj
			adj_LinO = batter['LinO'] * adj
			adj_PopO = batter['PopO'] * adj
			adj_FC = batter['FC'] * adj
			adj_FlyO = batter['FlyO'] * adj
			adj_DP = batter['DP'] * adj
			adj_K = batter['K'] * adj
			adj_TP = batter['TP'] * adj
			adj_CInf = batter['CInf'] * adj
			adj_FInf = batter['FInf'] * adj
			adj_E = batter['E'] * adj
			adj_HBP = batter['HBP'] * adj
			adj_IBB = batter['IBB'] * adj
			adj_BB = batter['BB'] * adj
			adj_Sac = batter['Sac'] * adj

			db.batter_PA_daily.update(
			{
				'playerID': playerID,
				'date' : gdate,
			},
			{ '$set': {
				'AB_adj' : adj_AB,
				'1B_adj' : adj_1B,
				'2B_adj' : adj_2B,
				'3B_adj' : adj_3B,
				'HR_adj' : adj_HR,
				'H_adj' : adj_H,
				'BInf_adj' : adj_BInf,
				'GndO_adj' : adj_GndO,
				'Bunt_adj' : adj_Bunt,
				'LinO_adj' : adj_LinO,
				'PopO_adj' : adj_PopO,
				'FC_adj' : adj_FC,
				'FlyO_adj' : adj_FlyO,
				'DP_adj' : adj_DP,
				'K_adj' : adj_K,
				'TP_adj' : adj_TP,
				'CInf_adj' : adj_CInf,
				'FInf_adj' : adj_FInf,
				'E_adj' : adj_E,
				'HBP_adj' : adj_HBP,
				'IBB_adj' : adj_IBB,
				'BB_adj' : adj_BB,
				'Sac_adj' : adj_Sac
			}})

		for pitcher in pitcherDailys:
			playerID = pitcher['playerID']
			adj_AB = pitcher['AB'] * adj
			adj_1B = pitcher['1Bfac'] * adj
			adj_2B = pitcher['2Bfac'] * adj
			adj_3B = pitcher['3Bfac'] * adj
			adj_HR = pitcher['HRfac'] * adj
			adj_H = pitcher['Hfac'] * adj
			adj_BInf = pitcher['BInf'] * adj
			adj_GndO = pitcher['GndO'] * adj
			adj_Bunt = pitcher['Bunt'] * adj
			adj_LinO = pitcher['LinO'] * adj
			adj_PopO = pitcher['PopO'] * adj
			adj_FC = pitcher['FC'] * adj
			adj_FlyO = pitcher['FlyO'] * adj
			adj_DP = pitcher['DP'] * adj
			adj_K = pitcher['K'] * adj
			adj_TP = pitcher['TP'] * adj
			adj_CInf = pitcher['CInf'] * adj
			adj_FInf = pitcher['FInf'] * adj
			adj_E = pitcher['E'] * adj
			adj_HBP = pitcher['HBP'] * adj
			adj_IBB = pitcher['IBB'] * adj
			adj_BB = pitcher['BB'] * adj
			adj_Sac = pitcher['Sac'] * adj

			db.pitcher_PA_daily.update(
			{
				'playerID': playerID,
				'date' : gdate,
			},
			{ '$set': {
				'AB_adj' : adj_AB,
				'1B_adj' : adj_1B,
				'2B_adj' : adj_2B,
				'3B_adj' : adj_3B,
				'HR_adj' : adj_HR,
				'H_adj' : adj_H,
				'BInf_adj' : adj_BInf,
				'GndO_adj' : adj_GndO,
				'Bunt_adj' : adj_Bunt,
				'LinO_adj' : adj_LinO,
				'PopO_adj' : adj_PopO,
				'FC_adj' : adj_FC,
				'FlyO_adj' : adj_FlyO,
				'DP_adj' : adj_DP,
				'K_adj' : adj_K,
				'TP_adj' : adj_TP,
				'CInf_adj' : adj_CInf,
				'FInf_adj' : adj_FInf,
				'E_adj' : adj_E,
				'HBP_adj' : adj_HBP,
				'IBB_adj' : adj_IBB,
				'BB_adj' : adj_BB,
				'Sac_adj' : adj_Sac
			}})

		adj = adj - 1
		print adj
