# WELCOME
"""
Introduction:
- prime methods
"""

import prime_finders


def oddPrimesVsNonPrimes(maxCheck) :
	"""
	- bPH-based print function
	- checks length of prime to non odd prime
	"""

	print('# of primes:',len(prime_finders.brutePrimesHard(maxCheck)))
	print('# of non-prime odds:',len(prime_finders.bruteOddNonPrimes(maxCheck)))


def findDifferenceList(l) :
	"""
	- general (hence 'l') method of discovering a list of CONSECUTIVE differences between entries of original list
	"""

	differenceList = []
	for i in range(1,len(l)) :
		differenceList.append(l[i] - l[i-1])
		print(f'Difference between {l[i]} and {l[i-1]}: {l[i]-l[i-1]}')

	assert len(differenceList) == len(l) - 1
	return differenceList


def findSpecDiff_PrintSpec(twoFactor,l) :
	"""
	- generates the number of CONSECUTIVE primes if their difference is the value of 'twoFactor'
	- twoFactor implies that the value of the difference between primes will always be an even integer

	- print version
	"""

	occurenceCounter = 0

	for i in range(1,len(l)) :
		if l[i] - l[i-1] == twoFactor :	
			print(f'{l[i]-l[i-1]} between {l[i]} and {l[i-1]}')
			occurenceCounter += 1

	return occurenceCounter


def findSpecDiffList_MidSpec(twoFactor,l) :
	"""
	- generates list of average of CONSECUTIVE primes whose difference is of value 'twoFactor'
	- if 'twoFactor' value is not divisble by 2, things might start looking funky
	"""

	midList = []

	for i in range(1,len(l)) :
		if l[i] - l[i-1] == twoFactor :	
			midList.append(l[i-1] + (twoFactor // 2)) # FIXME : can make more efficient / alternatives...

	return midList


def findSpecDiffList_MidSpec_SuperSpec(twoFactor,l) :
	"""
	"""

	midListSuper  = []

	for i in range(1,len(l)) :
		if l[i] - l[i-1] == twoFactor :	
			midListSuper.append((l[i-1] + (twoFactor / 2)) /2)

	return midListSuper


def findSpecDiffList_MidSpec_SuperSpec_DoubleSpec(twoFactor,l) :
	"""
	"""

	midList = []

	for i in range(1,len(l)) :
		if l[i] - l[i-1] == twoFactor :	
			midList.append(((l[i-1] + (twoFactor // 2)) //2) //3) 

	return midList

# MAIN STUFF #

if __name__ == '__main__' :

	print(dir(prime_finders))
	print(prime_finders.__spec__)

	"""
	user_in = int(input('Enter value:\n'))
	testList = []

	k = 0

	for j in (findSpecDiffList_MidSpec_SuperSpec_DoubleSpec(2,prime_finders.brutePrimesHard(user_in))) :
		testList.append(j-k)
		k = j


	print(f'Voila, here is your spaghetti:\n{findSpecDiffList_MidSpec_SuperSpec_DoubleSpec(2,prime_finders.brutePrimesHard(user_in))}')

	print(testList)
	"""