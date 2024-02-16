"""

Lets try to generate primes better!

The idea behind this generator:

Once you know 2 is a prime, you can
skip checking every 2nd number
to check if its prime cuz its
just a multiple of 2 (a prime)

Same with 3, once you know 3 is a
prime, you can skip checking every 3rd
number (just a multiple of 3, therefore
not prime!)

So once a prime is found (after skipping
numbers due to being multiples or whatever)
start skipping every that prime number
when checking

The best case would be that this program
just hops from prime to prime, never landing
on a non-prime number (no need to check all
the non-prime numbers between the primes, they
are just multiples of previous primes we know
about)

2
+1
3
+2
5
+2
7
+4
11
+2
13
+4
17
+2
19
+4
23
+6
29
+2
31
+6
37
+4
41
+2
43
+4
47

First we'll do it with a list,
then we'll make one that can
skip numbers on the fly


"""

from factorizerprinter import isPrime

#def primeGenerator(numToGenerate):
#	for i in range(0, numToGenerate):


def primeLister2(maxNum):
	tempList = []
	for i in range(0, maxNum+1):
		tempList.append(i)
	for i in tempList:
		if i == 1:
			tempList[i] = 0
			continue
		if i != 0:
			#print("Prime found: " + str(i))
			j = 2*i
			while j <= maxNum:
				tempList[j] = 0
				j += i
	#print(tempList)
	returnList = []
	for k in tempList:
		if k != 0:
			returnList.append(k)
	#print(returnList)
	return returnList


def primeChecker(listOfPrimes): # checks if my prime generator function
	for i in listOfPrimes:      # actually generates primes
		if not isPrime(i):
			print("Failed :(")
			print(i)
			return
	print("Success!!!")


def primeLogarthims(incrementSize):
	for i in range(0, 300):
		numPrimes = str(len(primeLister2((i+1)*incrementSize)) - 
			len(primeLister2(i*incrementSize)))
		print("Number of primes from " + str(i*incrementSize) + 
			" to " + str((i+1)*incrementSize) + ": " + numPrimes)






#primeChecker(primeLister2(10000))
#print(primeLister2(10000))

primeLogarthims(1000)