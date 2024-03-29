def findPrimesLength(length) : #####WIP#####
	"""
	- generates a list of prime integers
	- length of list corresponds to integer input
	- function is NOT optimized

	:parameters - 'length' - integer
	:return - 'primeList' - list
	"""

	# > initialize variables
	primeList = [2]
	primeCount = 0
	value = 3

	# > loop appends primes
	# > breaks when the list reaches desired length

	while True :
		for i in primeList :
			primeList.append(value)
			i += 1

		value += 1

		if primeCount == length :
			break

	assert primeCount == len(primeList)

	return (primeList)


def findPrimesMax(maxCheck) : #####WIP#####
	"""
	- generates list of prime integers
	- length of list depends on how many primes in the range ( 2 , 'maxCheck' )
	- function is NOT optimized

	:parameters - 'maxCheck' - int
	:return - 'primeList' - list
	"""

	primeList = []

	return (primeList)


def brutePrimesHard(maxCheck) :
	"""
	- less eloquent way of building primes into a list
	- list includes primes from 2 to 'maxCheck' value (inclusive)
	- somewhat brute-forcey

	:parameter(s) - 'maxCheck' - int
	:return - 'primeList' - list
	"""

	primeList = []
	for i in range(2,maxCheck+1) : # iterates 2, 3, 4,...
		for prime in primeList : # iterates primes
			if i % prime != 0 or primeList == [] :
				continue
			else :
				break
		else :
			primeList.append(i)

	return (primeList)

def bruteOddNonPrimes(maxCheck) :
	"""
	- less eloquent way of finding non prime odds 
	- puts non prime odds into a list
	- requires and is based on 'brutePrimesHard'
	"""

	nonPrimeList = []
	primeCompare = brutePrimesHard(maxCheck)

	for i in range(2,maxCheck+1) :
		if not(i in primeCompare) and not(i % 2 == 0) :
			nonPrimeList.append(i)

	return (nonPrimeList)
	

def iterPrimesLength(length) : #####WIP#####
	"""
	"""
	# FIXME


def iterPrimesMax(maxCheck) : #####WIP#####
	"""
	"""
	# FIX ME


def iterBrutePrimes(maxCheck) : #####WIP#####

	for i in range(2,maxCheck) :
		if True :
			pass #FIX ME