import boto3
import json
from random import randint
import time

s3 = boto3.resource('s3')

init = {
	'gameon':True,
	'inning':1,
	'side':1,
	'outs':0,
	'firstbase':None,
	'secondbase':None,
	'thirdbase':None,
	'homeRuns':0,
	'awayRuns':0,
	'homeOrder':1,
	'awayOrder':1,
}

params_key = s3.Object('mlbsim', 'params.json')
params_file = params_key.get()["Body"]
params = json.load(params_file)
#with open('params.json') as params_file:    
#   params = json.load(params_file)
init.update(params)

home_key = s3.Object('mlbsim', 'was.json')
home_file = home_key.get()["Body"]
homeLineup = json.load(home_file)

away_key = s3.Object('mlbsim', 'nyn.json')
away_file = away_key.get()["Body"]
awayLineup = json.load(away_file)

def atBat( params ):
	atbat = True
	balls = 0
	strikes = 0
	inplay = False

	while(atbat):
		pitch = randint(1, 1000) 
		if(pitch >= params['strikeRate']):
			balls += 1
		else:
			contact = randint(1, 1000)
			if(contact <= params['contactRate']):
				foul = randint(1, 1000)
				if (foul <= params['foulRate']):
					if(strikes < 2):
						strikes += 1
				else:
					inplay = True
			else:
				strikes += 1
		if(balls == 4):
			print "Walk"
			params = walk(params)
			atbat = False
		elif(strikes == 3):
			params['outs'] += 1
			atbat = False
			print "Strikeout" + str(params['outs'])
		elif(inplay):
			print "In Play"
			params = ballinplay(params)
			atbat = False
	return(params)

def walk(params):
	runs = 0
	firstbase = params['firstbase']
	secondbase = params['secondbase']
	thirdbase = params['thirdbase']
	if(firstbase and secondbase and thirdbase):
		thirdbase = 1
		secondbase = 1
		firstbase = 1
		runs += 1
		print "Run!"
		print "Bases Loaded"
	elif(firstbase and secondbase):
		thirdbase = 1
		secondbase = 1
		firstbase  = 1
		print "Bases Loaded"
	elif(firstbase):
		secondbase = 1
		firstbase = 1
		print "Runners on First and Second"
	else:
		firstbase = 1
		print "Runner on First"
	if(runs > 0):
		if(params['side'] == 1):
			params['awayRuns'] += runs
		else:
			params['homeRuns'] += runs
	params['firstbase'] = firstbase
	params['secondbase'] = secondbase
	params['thirdbase'] = thirdbase
	return(params)

def ballinplay(params):
	runs = 0
	firstbase = params['firstbase']
	secondbase = params['secondbase']
	thirdbase = params['thirdbase']
	hit = randint(1,1000)
	if (hit > params['hitRate']):
		if(hit > params['flyRate']):
			params['outs'] += 1
			print "Fly Out" + str(params['outs'])
		else:
			if(firstbase and secondbase and thirdbase and params['outs'] < 2):
				firstbase= None
				runs += 1
			elif(firstbase and secondbase):
				thirdbase = 1
				firstbase = None
			elif(firstbase):
				secondbase = 1
				firstbase = None
			params['outs'] += 1
			print "Ground Out" + str(params['outs'])
	elif(hit <= params['tripleRate']):
		print "Triple"
		if(thirdbase):
			thirdbase = 1
			runs += 1
			print "Run!"
		if(secondbase):
			secondbase = None
			thirdbase  = 1
			runs += 1
			print "Run!"
		if(firstbase):
			firstbase = None
			thirdbase = 1
			runs += 1
			print "Run!"
		else:
			thirdbase = 1
	elif(hit <= params['hrRate']):
		print "Home Run!"
		if(thirdbase):
			thirdbase = None
			runs += 1
			print "Run!"
		if(secondbase):
			secondbase = None
			runs += 1
			print "Run!"
		if(firstbase):
			firstbase = None
			runs += 1
			print "Run!"
		runs += 1
	elif(hit <= params['doubleRate']):
		print "Double!"
		if(thirdbase):
			secondbase = 1
			thirdbase = None
			runs += 1
			print "Run!"
		if(secondbase):
			secondbase = 1
			runs += 1
			print "Run!"
		if(firstbase):
			firstbase = None
			secondbase = 1
			runs += 1
			print "Run!"
		else:
			secondbase = 1
	elif(hit <= params['hitRate']):
		print "Base Hit"
		if(thirdbase):
			thirdbase = None
			firstbase = 1
			runs += 1
			print "Run!"
		if(secondbase):
			secondbase = None
			firstbase  = 1
			runs += 1
			print "Run!"
		if(firstbase):
			thirdbase = 1
			firstbase = 1
		else:
			firstbase = 1
	if(runs > 0):
		if(params['side'] == 1):
			params['awayRuns'] += runs
		else:
			params['homeRuns'] += runs
	params['firstbase'] = firstbase
	params['secondbase'] = secondbase
	params['thirdbase'] = thirdbase
	return(params)

def nextBatter(params,homeLineup,awayLineup):
	if(params['side'] == 2):
		order = params['homeOrder']
		batter = homeLineup[str(order)]
		if(params['homeOrder'] < 9):
			params['homeOrder'] += 1
		else:
			params['homeOrder'] = 1
		
	else:
		order = params['awayOrder']
		batter = awayLineup[str(order)]
		if(params['awayOrder'] < 9):
			params['awayOrder'] += 1
		else:
			params['awayOrder'] = 1
	print batter
	return params

def game(params,homeLineup,awayLineup):
	while(params['gameon']):
		params = nextBatter(params,homeLineup,awayLineup)
		params = atBat( params )
		if(params['inning'] >= 9 and params['side'] == 2 and params['homeRuns'] > params['awayRuns']):
			params['gameon'] = False
		if(params['outs'] == 3):
			params['firstbase'] = None
			params['secondbase'] = None
			params['thirdbase'] = None
			print "Inning Over"
			if(params['side']) == 1:
				if(params['inning'] >= 9):
					if(params['homeRuns'] > params['awayRuns']):
						params['gameon'] = False
					else:
						params['side'] = 2
						params['outs'] = 0
				else:
					params['side'] = 2
					params['outs'] = 0
			else:
				if(params['inning'] >= 9):
					if(params['awayRuns'] == params['homeRuns']):
						params['inning'] += 1
						params['outs'] = 0
						print "Inning" + str(params['inning'])
					else:
						params['gameon'] = False
				else:
					params['side'] = 1
					params['inning'] += 1
					params['outs'] = 0
					print "Inning" + str(params['inning'])
	return(params)

status = game(init,homeLineup,awayLineup)
#print status

gameLog = {
	'id':str(time.time()),
	'home':'was',
	'away':'nyn',
	'homeR':status["homeRuns"],
	'awayR':status["awayRuns"]	
}

gameLogJSON = json.dumps(gameLog)

log_key = s3.Object('mlbsim', 'log/games.json')
log_file = log_key.get()["Body"].read()
newbody = gameLogJSON + "\n" + log_file
s3.Bucket('mlbsim').put_object(Key='log/games.json', Body=newbody)