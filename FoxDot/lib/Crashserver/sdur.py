from ..Patterns import P, Pattern
import random

##### SDur by Quantuum #####
def SDur(target):
	sr = random.SystemRandom()
	indexes = random.randint(1,target+4)
	dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
	list=[]
	for i in range(0,indexes):
			if target%2 == 0:
					a = random.randint(1,target/2)/sr.choice(dividers)
			else:
					a = random.randint(1,(target-1)/2)/sr.choice(dividers)
			if sum(list)+a < target/2:
					list.append(a)
			if sum(list)+a < target:
					list.append(a)
	list.append(target-sum(list))
	return P[list].shuffle() # always return a list of durations with total duration equals target

# variation giving shorter durations
def SmDur(target):
	sr = random.SystemRandom()
	indexes = random.randint(1,target+4)
	dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
	list=[]
	for i in range(0,indexes):
			if target%2 == 0:
					a = random.randint(1,target/2)/sr.choice(dividers)
			else:
					a = random.randint(1,(target-1)/2)/sr.choice(dividers)
			if sum(list)+a < target/2:
					list.append(a)
			if sum(list)+a/2 < target:
					list.append(a/2)
	list.append(target-sum(list))
	return P[list].shuffle() # always return a list of durations with total duration equals target

# a variation with score-like durations
def ScDur(target):
	sr = random.SystemRandom()
	indexes = random.randint(1,target+4)
	standards = [0.25,0.375,0.75,0.5,1,2,3,4] # standard dur values found in scores
	dividers = [1,1,2] # skip 1/4 and 1/8 (comes after)
	list=[]
	for i in range(0,indexes):
			if target%2 == 0:
					a = random.randint(1,target/2)/sr.choice(dividers)
			else:
					a = random.randint(1,(target-1)/2)/sr.choice(dividers)
			if sum(list)+a < target/4:
					list.append(a)
			if sum(list)+a/2 < target/2:
					list.append(a/2)
			if sum(list)+a < target:
					list.append(a)
			if sum(list)+a/4 < target:
					list.append(a/4)
	if sum(list) < target:
			for i in range(0,len(standards)):
					if target-sum(list)%standards[i] != 0 and standards[i] < target-sum(list):
							list.append(standards[i])
			if sum(list) < target:
					list.append(target-sum(list))
	return P[list].shuffle() # always return a list of durations with total duration equals target
