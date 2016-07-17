import datetime
import mongo_connect

db = mongo_connect.connect()
from datetime import datetime

batterDaily = db.batter_PA_daily.find( { "date": {"$gt": 20160101 }} ).sort([("playerID", 1),("throws", 1),("date", 1)])
pitcherDaily = db.pitcher_PA_daily.find( { "date": {"$gt": 20160101 }} ).sort([("playerID", 1),("stand", 1),("date", 1)])


season = {}
def reset(season):
	season['AB'] = 0
	season['1B'] = 0
	season['2B'] = 0
	season['3B'] = 0
	season['HR'] = 0
	season['H'] = 0
	season['BInf'] = 0
	season['GndO'] = 0
	season['Bunt'] = 0
	season['LinO'] = 0
	season['PopO'] = 0
	season['FC'] = 0
	season['FlyO'] = 0
	season['DP'] = 0
	season['K'] = 0
	season['TP'] = 0
	season['CInf'] = 0
	season['FInf'] = 0
	season['E'] = 0
	season['HBP'] = 0
	season['IBB'] = 0
	season['BB'] = 0
	season['Sac'] = 0
	season['AB_adj'] = 0
	season['1B_adj'] = 0
	season['2B_adj'] = 0
	season['3B_adj'] = 0
	season['HR_adj'] = 0
	season['H_adj'] = 0
	season['BInf_adj'] = 0
	season['GndO_adj'] = 0
	season['Bunt_adj'] = 0
	season['LinO_adj'] = 0
	season['PopO_adj'] = 0
	season['FC_adj'] = 0
	season['FlyO_adj'] = 0
	season['DP_adj'] = 0
	season['K_adj'] = 0
	season['TP_adj'] = 0
	season['CInf_adj'] = 0
	season['FInf_adj'] = 0
	season['E_adj'] = 0
	season['HBP_adj'] = 0
	season['IBB_adj'] = 0
	season['BB_adj'] = 0
	season['Sac_adj'] = 0
	return season

def loadSeasonBatter(season,playerID):
	db.batter_season.insert(
		{
			'playerID': int(playerID),
			'throws' : season['throws'],
			'AB' : season['AB'],
			'1B' : season['1B'],
			'2B' : season['2B'],
			'3B' : season['3B'],
			'HR' : season['HR'],
			'H' : season['H'],
			'BInf' : season['BInf'],
			'GndO' : season['GndO'],
			'Bunt' : season['Bunt'],
			'LinO' : season['LinO'],
			'PopO' : season['PopO'],
			'FC' : season['FC'],
			'FlyO' : season['FlyO'],
			'DP' : season['DP'],
			'K' : season['K'],
			'TP' : season['TP'],
			'CInf' : season['CInf'],
			'FInf' : season['FInf'],
			'E' : season['E'],
			'HBP' : season['HBP'],
			'IBB' : season['IBB'],
			'BB' : season['BB'],
			'Sac' : season['Sac'],
			'AB_adj' : season['AB_adj'],
			'1B_adj' : season['1B_adj'],
			'2B_adj' : season['2B_adj'],
			'3B_adj' : season['3B_adj'],
			'HR_adj' : season['HR_adj'],
			'H_adj' : season['H_adj'],
			'BInf_adj' : season['BInf_adj'],
			'GndO_adj' : season['GndO_adj'],
			'Bunt_adj' : season['Bunt_adj'],
			'LinO_adj' : season['LinO_adj'],
			'PopO_adj' : season['PopO_adj'],
			'FC_adj' : season['FC_adj'],
			'FlyO_adj' : season['FlyO_adj'],
			'DP_adj' : season['DP_adj'],
			'K_adj' : season['K_adj'],
			'TP_adj' : season['TP_adj'],
			'CInf_adj' : season['CInf_adj'],
			'FInf_adj' : season['FInf_adj'],
			'E_adj' : season['E_adj'],
			'HBP_adj' : season['HBP_adj'],
			'IBB_adj' : season['IBB_adj'],
			'BB_adj' : season['BB_adj'],
			'Sac_adj' : season['Sac_adj'],
			'PA_adj' : season['PA_adj'],
			'OBP_adj' : season['OBP_adj'],
			'wOBA_adj' : season['wOBA_adj'],
			'SLG_adj' : season['SLG_adj'],
			'OPS_adj' : season['OPS_adj'],
			'1B_avg' : season['1B_avg'],
			'2B_avg' : season['2B_avg'],
			'3B_avg' : season['3B_avg'],
			'HR_avg' : season['HR_avg'],
			'H_avg' : season['H_avg'],
			'BInf_avg' : season['BInf_avg'],
			'GndO_avg' : season['GndO_avg'],
			'Bunt_avg' : season['Bunt_avg'],
			'LinO_avg' : season['LinO_avg'],
			'PopO_avg' : season['PopO_avg'],
			'FlyO_avg' : season['FlyO_avg'],
			'DP_avg' : season['DP_avg'],
			'K_avg' : season['K_avg'],
			'TP_avg' : season['TP_avg'],
			'CInf_avg' : season['CInf_avg'],
			'FInf_avg' : season['FInf_avg'],
			'E_avg' : season['E_avg'],
			'HBP_avg' : season['HBP_avg'],
			'IBB_avg' : season['IBB_avg'],
			'BB_avg' : season['BB_avg'],
			'Sac_avg' : season['Sac_avg']
		})

def loadSeasonPitcher(season,playerID):
	db.pitcher_season.insert(
		{
			'playerID': int(playerID),
			'stand' : season['stand'],
			'AB' : season['AB'],
			'1B' : season['1B'],
			'2B' : season['2B'],
			'3B' : season['3B'],
			'HR' : season['HR'],
			'H' : season['H'],
			'BInf' : season['BInf'],
			'GndO' : season['GndO'],
			'Bunt' : season['Bunt'],
			'LinO' : season['LinO'],
			'PopO' : season['PopO'],
			'FC' : season['FC'],
			'FlyO' : season['FlyO'],
			'DP' : season['DP'],
			'K' : season['K'],
			'TP' : season['TP'],
			'CInf' : season['CInf'],
			'FInf' : season['FInf'],
			'E' : season['E'],
			'HBP' : season['HBP'],
			'IBB' : season['IBB'],
			'BB' : season['BB'],
			'Sac' : season['Sac'],
			'AB_adj' : season['AB_adj'],
			'1B_adj' : season['1B_adj'],
			'2B_adj' : season['2B_adj'],
			'3B_adj' : season['3B_adj'],
			'HR_adj' : season['HR_adj'],
			'H_adj' : season['H_adj'],
			'BInf_adj' : season['BInf_adj'],
			'GndO_adj' : season['GndO_adj'],
			'Bunt_adj' : season['Bunt_adj'],
			'LinO_adj' : season['LinO_adj'],
			'PopO_adj' : season['PopO_adj'],
			'FC_adj' : season['FC_adj'],
			'FlyO_adj' : season['FlyO_adj'],
			'DP_adj' : season['DP_adj'],
			'K_adj' : season['K_adj'],
			'TP_adj' : season['TP_adj'],
			'CInf_adj' : season['CInf_adj'],
			'FInf_adj' : season['FInf_adj'],
			'E_adj' : season['E_adj'],
			'HBP_adj' : season['HBP_adj'],
			'IBB_adj' : season['IBB_adj'],
			'BB_adj' : season['BB_adj'],
			'Sac_adj' : season['Sac_adj'],
			'PA_adj' : season['PA_adj'],
			'OBP_adj' : season['OBP_adj'],
			'wOBA_adj' : season['wOBA_adj'],
			'SLG_adj' : season['SLG_adj'],
			'OPS_adj' : season['OPS_adj'],
			'1B_avg' : season['1B_avg'],
			'2B_avg' : season['2B_avg'],
			'3B_avg' : season['3B_avg'],
			'HR_avg' : season['HR_avg'],
			'H_avg' : season['H_avg'],
			'BInf_avg' : season['BInf_avg'],
			'GndO_avg' : season['GndO_avg'],
			'Bunt_avg' : season['Bunt_avg'],
			'LinO_avg' : season['LinO_avg'],
			'PopO_avg' : season['PopO_avg'],
			'FlyO_avg' : season['FlyO_avg'],
			'DP_avg' : season['DP_avg'],
			'K_avg' : season['K_avg'],
			'TP_avg' : season['TP_avg'],
			'CInf_avg' : season['CInf_avg'],
			'FInf_avg' : season['FInf_avg'],
			'E_avg' : season['E_avg'],
			'HBP_avg' : season['HBP_avg'],
			'IBB_avg' : season['IBB_avg'],
			'BB_avg' : season['BB_avg'],
			'Sac_avg' : season['Sac_avg']
		})

db.batter_season.remove({})
db.pitcher_season.remove({})
season = reset(season)
lastPlayerID = 0
lastThrows = ""
for daily in batterDaily:
	playerID = daily['playerID']
	throws = daily['throws']
	print playerID
	print throws
	print date
	if(lastPlayerID != 0 and (playerID != lastPlayerID or (playerID == lastPlayerID and throws != lastThrows))):
		loadSeasonBatter(season,lastPlayerID)
		season = reset(season)
	lastPlayerID = playerID
	lastThrows = throws
	season['throws'] = throws
	season['AB'] = season['AB'] + daily['AB']
	season['1B'] = season['1B'] + daily['1B']
	season['2B'] = season['2B'] + daily['2B']
	season['3B'] = season['3B'] + daily['3B']
	season['HR'] = season['HR'] + daily['HR']
	season['H'] = season['H'] + daily['H']
	season['BInf'] = season['BInf'] + daily['BInf']
	season['GndO'] = season['GndO'] + daily['GndO']
	season['Bunt'] = season['Bunt'] + daily['Bunt']
	season['LinO'] = season['LinO'] + daily['LinO']
	season['PopO'] = season['PopO'] + daily['PopO']
	season['FC'] = season['FC'] + daily['FC']
	season['FlyO'] = season['FlyO'] + daily['FlyO']
	season['DP'] = season['DP'] + daily['DP']
	season['K'] = season['K'] + daily['K']
	season['TP'] = season['TP'] + daily['TP']
	season['CInf'] = season['CInf'] + daily['CInf']
	season['FInf'] = season['FInf'] + daily['FInf']
	season['E'] = season['E'] + daily['E']
	season['HBP'] = season['HBP'] + daily['HBP']
	season['IBB'] = season['IBB'] + daily['IBB']
	season['BB'] = season['BB'] + daily['BB']
	season['Sac'] = season['Sac'] + daily['Sac']
	season['AB_adj'] = season['AB_adj'] + daily['AB_adj']
	season['1B_adj'] = season['1B_adj'] + daily['1B_adj']
	season['2B_adj'] = season['2B_adj'] + daily['2B_adj']
	season['3B_adj'] = season['3B_adj'] + daily['3B_adj']
	season['HR_adj'] = season['HR_adj'] + daily['HR_adj']
	season['H_adj'] = season['H_adj'] + daily['H_adj']
	season['BInf_adj'] = season['BInf_adj'] + daily['BInf_adj']
	season['GndO_adj'] = season['GndO_adj'] + daily['GndO_adj']
	season['Bunt_adj'] = season['Bunt_adj'] + daily['Bunt_adj']
	season['LinO_adj'] = season['LinO_adj'] + daily['LinO_adj']
	season['PopO_adj'] = season['PopO_adj'] + daily['PopO_adj']
	season['FC_adj'] = season['FC_adj'] + daily['FC_adj']
	season['FlyO_adj'] = season['FlyO_adj'] + daily['FlyO_adj']
	season['DP_adj'] = season['DP_adj'] + daily['DP_adj']
	season['K_adj'] = season['K_adj'] + daily['K_adj']
	season['TP_adj'] = season['TP_adj'] + daily['TP_adj']
	season['CInf_adj'] = season['CInf_adj'] + daily['CInf_adj']
	season['FInf_adj'] = season['FInf_adj'] + daily['FInf_adj']
	season['E_adj'] = season['E_adj'] + daily['E_adj']
	season['HBP_adj'] = season['HBP_adj'] + daily['HBP_adj']
	season['IBB_adj'] = season['IBB_adj'] + daily['IBB_adj']
	season['BB_adj'] = season['BB_adj'] + daily['BB_adj']
	season['Sac_adj'] = season['Sac_adj'] + daily['Sac_adj']
	season['PA_adj'] = season['AB_adj'] + season['CInf_adj'] + season['FInf_adj'] + season['E_adj'] + season['HBP_adj'] + season['BB_adj'] + season['Sac_adj']
	if(season['PA_adj'] > 0):
		season['OBP_adj'] = float(season['H_adj'] + season['CInf_adj'] + season['FInf_adj'] + season['E_adj'] + season['HBP_adj'] + season['BB_adj'])/season['PA_adj']
		season['wOBA_adj'] = float(season['BB_adj']*0.691 + season['HBP_adj']*0.722 + season['1B_adj']*0.879 + season['2B_adj']*1.241 + season['3B_adj']*1.567 + season['HR_adj']*2.01)/season['PA_adj']
	else:
		season['OBP_adj'] = 0
	if(season['AB_adj'] > 0):
		season['SLG_adj'] = float(season['1B_adj'] + season['2B_adj']*2 + season['3B_adj']*3 + season['HR_adj']*4) / season['AB_adj']
	else:
		season['SLG_adj'] = 0
	season['OPS_adj'] = season['OBP_adj'] + season['SLG_adj']
	if(season['PA_adj'] > 0):
		season['1B_avg'] = float(season['1B_adj']) / season['PA_adj']
		season['2B_avg'] = float(season['2B_adj']) / season['PA_adj']
		season['3B_avg'] = float(season['3B_adj']) / season['PA_adj']
		season['HR_avg'] = float(season['HR_adj']) / season['PA_adj']
		season['H_avg'] = float(season['H_adj']) / season['PA_adj']
		season['BInf_avg'] = float(season['BInf_adj']) / season['PA_adj']
		season['GndO_avg'] = float(season['GndO_adj']) / season['PA_adj']
		season['Bunt_avg'] = float(season['Bunt_adj']) / season['PA_adj']
		season['LinO_avg'] = float(season['LinO_adj']) / season['PA_adj']
		season['PopO_avg'] = float(season['PopO_adj']) / season['PA_adj']
		season['FlyO_avg'] = float(season['FlyO_adj']) / season['PA_adj']
		season['DP_avg'] = float(season['DP_adj']) / season['PA_adj']
		season['K_avg'] = float(season['K_adj']) / season['PA_adj']
		season['TP_avg'] = float(season['TP_adj']) / season['PA_adj']
		season['CInf_avg'] = float(season['CInf_adj']) / season['PA_adj']
		season['FInf_avg'] = float(season['FInf_adj']) / season['PA_adj']
		season['E_avg'] = float(season['E_adj']) / season['PA_adj']
		season['HBP_avg'] = float(season['HBP_adj']) / season['PA_adj']
		season['IBB_avg'] = float(season['IBB_adj']) / season['PA_adj']
		season['BB_avg'] = float(season['BB_adj']) / season['PA_adj']
		season['Sac_avg'] = float(season['Sac_adj']) / season['PA_adj']
loadSeasonBatter(season,lastPlayerID)

season = reset(season)
lastPlayerID = 0
lastStand = ""
for daily in pitcherDaily:
	playerID = daily['playerID']
	stand = daily['stand']
	if(lastPlayerID != 0 and (playerID != lastPlayerID or (playerID == lastPlayerID and stand != lastStand))):
		print playerID
		print stand
		loadSeasonPitcher(season,lastPlayerID)
		season = reset(season)
	lastPlayerID = playerID
	lastStand = stand
	season['stand'] = stand
	season['AB'] = season['AB'] + daily['AB']
	season['1B'] = season['1B'] + daily['1B']
	season['2B'] = season['2B'] + daily['2B']
	season['3B'] = season['3B'] + daily['3B']
	season['HR'] = season['HR'] + daily['HR']
	season['H'] = season['H'] + daily['H']
	season['BInf'] = season['BInf'] + daily['BInf']
	season['GndO'] = season['GndO'] + daily['GndO']
	season['Bunt'] = season['Bunt'] + daily['Bunt']
	season['LinO'] = season['LinO'] + daily['LinO']
	season['PopO'] = season['PopO'] + daily['PopO']
	season['FC'] = season['FC'] + daily['FC']
	season['FlyO'] = season['FlyO'] + daily['FlyO']
	season['DP'] = season['DP'] + daily['DP']
	season['K'] = season['K'] + daily['K']
	season['TP'] = season['TP'] + daily['TP']
	season['CInf'] = season['CInf'] + daily['CInf']
	season['FInf'] = season['FInf'] + daily['FInf']
	season['E'] = season['E'] + daily['E']
	season['HBP'] = season['HBP'] + daily['HBP']
	season['IBB'] = season['IBB'] + daily['IBB']
	season['BB'] = season['BB'] + daily['BB']
	season['Sac'] = season['Sac'] + daily['Sac']
	season['AB_adj'] = season['AB_adj'] + daily['AB_adj']
	season['1B_adj'] = season['1B_adj'] + daily['1B_adj']
	season['2B_adj'] = season['2B_adj'] + daily['2B_adj']
	season['3B_adj'] = season['3B_adj'] + daily['3B_adj']
	season['HR_adj'] = season['HR_adj'] + daily['HR_adj']
	season['H_adj'] = season['H_adj'] + daily['H_adj']
	season['BInf_adj'] = season['BInf_adj'] + daily['BInf_adj']
	season['GndO_adj'] = season['GndO_adj'] + daily['GndO_adj']
	season['Bunt_adj'] = season['Bunt_adj'] + daily['Bunt_adj']
	season['LinO_adj'] = season['LinO_adj'] + daily['LinO_adj']
	season['PopO_adj'] = season['PopO_adj'] + daily['PopO_adj']
	season['FC_adj'] = season['FC_adj'] + daily['FC_adj']
	season['FlyO_adj'] = season['FlyO_adj'] + daily['FlyO_adj']
	season['DP_adj'] = season['DP_adj'] + daily['DP_adj']
	season['K_adj'] = season['K_adj'] + daily['K_adj']
	season['TP_adj'] = season['TP_adj'] + daily['TP_adj']
	season['CInf_adj'] = season['CInf_adj'] + daily['CInf_adj']
	season['FInf_adj'] = season['FInf_adj'] + daily['FInf_adj']
	season['E_adj'] = season['E_adj'] + daily['E_adj']
	season['HBP_adj'] = season['HBP_adj'] + daily['HBP_adj']
	season['IBB_adj'] = season['IBB_adj'] + daily['IBB_adj']
	season['BB_adj'] = season['BB_adj'] + daily['BB_adj']
	season['Sac_adj'] = season['Sac_adj'] + daily['Sac_adj']
	season['PA_adj'] = season['AB_adj'] + season['CInf_adj'] + season['FInf_adj'] + season['E_adj'] + season['HBP_adj'] + season['BB_adj'] + season['Sac_adj']
	if(season['PA_adj'] > 0):
		season['OBP_adj'] = float(season['H_adj'] + season['CInf_adj'] + season['FInf_adj'] + season['E_adj'] + season['HBP_adj'] + season['BB_adj'])/season['PA_adj']
		season['wOBA_adj'] = float(season['BB_adj']*0.691 + season['HBP_adj']*0.722 + season['1B_adj']*0.879 + season['2B_adj']*1.241 + season['3B_adj']*1.567 + season['HR_adj']*2.01)/season['PA_adj']
	
	else:
		season['OBP_adj'] = 0
	if(season['AB_adj'] > 0):
		season['SLG_adj'] = float(season['1B_adj'] + season['2B_adj']*2 + season['3B_adj']*3 + season['HR_adj']*4) / season['AB_adj']
	else:
		season['SLG_adj'] = 0
	season['OPS_adj'] = season['OBP_adj'] + season['SLG_adj']
	if(season['PA_adj'] > 0):
		season['1B_avg'] = float(season['1B_adj']) / season['PA_adj']
		season['2B_avg'] = float(season['2B_adj']) / season['PA_adj']
		season['3B_avg'] = float(season['3B_adj']) / season['PA_adj']
		season['HR_avg'] = float(season['HR_adj']) / season['PA_adj']
		season['H_avg'] = float(season['H_adj']) / season['PA_adj']
		season['BInf_avg'] = float(season['BInf_adj']) / season['PA_adj']
		season['GndO_avg'] = float(season['GndO_adj']) / season['PA_adj']
		season['Bunt_avg'] = float(season['Bunt_adj']) / season['PA_adj']
		season['LinO_avg'] = float(season['LinO_adj']) / season['PA_adj']
		season['PopO_avg'] = float(season['PopO_adj']) / season['PA_adj']
		season['FlyO_avg'] = float(season['FlyO_adj']) / season['PA_adj']
		season['DP_avg'] = float(season['DP_adj']) / season['PA_adj']
		season['K_avg'] = float(season['K_adj']) / season['PA_adj']
		season['TP_avg'] = float(season['TP_adj']) / season['PA_adj']
		season['CInf_avg'] = float(season['CInf_adj']) / season['PA_adj']
		season['FInf_avg'] = float(season['FInf_adj']) / season['PA_adj']
		season['E_avg'] = float(season['E_adj']) / season['PA_adj']
		season['HBP_avg'] = float(season['HBP_adj']) / season['PA_adj']
		season['IBB_avg'] = float(season['IBB_adj']) / season['PA_adj']
		season['BB_avg'] = float(season['BB_adj']) / season['PA_adj']
		season['Sac_avg'] = float(season['Sac_adj']) / season['PA_adj']
loadSeasonPitcher(season,lastPlayerID)
print batterDaily.count()
