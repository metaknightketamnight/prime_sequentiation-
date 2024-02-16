import prime_finders

def oddPrimesVsNonPrimes(maxCheck) :
	print('# of primes:',len(brutePrimesHard(maxCheck)))
	print('# of non-prime odds:',len(bruteOddNonPrimes(maxCheck)))


def findDifferenceList(primeList) :
	differenceList = []
	for i in range(1,len(primeList)) :
		differenceList.append(primeList[i] - primeList[i-1])

	return differenceList

oddPrimesVsNonPrimes(5)
# print(findDifferenceList(brutePrimesHard(input())))