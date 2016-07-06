import random

bank = 50
rando = random.uniform(0, 1)

if(rando > 0.7):
	result = False
else:
	result = True

for x in range(0, 100):
	rando = random.uniform(0, 1)

	if(rando > 0.70):
		result = False
		bank = bank - (bank*0.25)
	else:
		result = True
		bank = bank + (bank*0.25*0.8)
	print int(bank)