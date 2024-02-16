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
	- general (hence 'l') method of discovering a list of differences between entries of original list
	"""
	differenceList = []
	for i in range(1,len(l)) :
		differenceList.append(l[i] - l[i-1])
		print(f'Difference between {l[i]} and {l[i-1]}: {l[i]-l[i-1]}')

	assert len(differenceList) == len(l) - 1
	return differenceList


user_in = int(input())
print(prime_finders.brutePrimesHard(user_in))
findDifferenceList(prime_finders.brutePrimesHard(user_in))
