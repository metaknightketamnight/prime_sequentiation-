#this files gonna print a bunch of prime factorizations fun

import math

def primeFactorization(factorNum): #not super efficient i know lol
	for i in range(2, math.ceil(math.sqrt(factorNum))+1):
		if factorNum%i == 0:
			return str(i) + " " + str(primeFactorization(int(factorNum/i)))
	return str(factorNum)

#primeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def isPrime(num): #returns true if prime, false otherwise
	if num == 2:  #special case cuz 2 fucks this up
		return True
	for i in range(2, math.ceil(math.sqrt(num))+1):
		if num%i ==  0:
			return False
	return True

def primeLister(max): #lists all primes below max
	primesList = [2]
	for i in range(2, max+1):
		if isPrime(i):
			primesList.append(i)
	return primesList

def primeSequentializer(inputNum): # prints out the prime serialization of a number (right-adjusted Ayman way)
	factorList = primeFactorization(inputNum).split(" ")
	#print(factorList)
	pList = primeLister(inputNum)
	#print(pList)
	outputList = []
	for i in range(0, len(pList)):
		outputList.append(0)
	#print(factorList)
	for i in range(len(pList)):
		#print(factorList.count(str(pList[i])))
		outputList[i] = factorList.count(str(pList[i]))
	outputList.reverse()
	outputString = ""
	leadingZeros = True
	for i in outputList:
		if i == 0:
			if leadingZeros:
				continue
			else:
				outputString = outputString + str(i)
		else:
			leadingZeros = False
			outputString = outputString + str(i)
	return outputString




#print(primeFactorization(144))
#print(math.ceil(math.sqrt(9)))
#print(primeLister(1000))
#print(primeSequentializer(100))
#print(primeSequentializer(534))

#for i in range(1, 1001):
#	print(primeSequentializer(i))

