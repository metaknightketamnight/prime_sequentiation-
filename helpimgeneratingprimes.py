"""

Let's generate primes EVEN BETTAHH

So you know how we previously talked about
the next prime being the next number that
isn't divisible by the primes we already have

We can "find" these next primes by creating a
multiple of the primes we have so far, then
adding 1

This way we're guaranteed to have a number
that isn't a multiple of the primes we have
previously generated! (1 doesn't count lol)

Example:

(Lets say we already know 2 is a prime cuz
this gets hella annoying otherwise)

2^1+1 = 3 < new prime!

Another thing I just notices is that 2 MUST
be in the generated number we add 1 to
Because if it isn't, then the generated
number will be made up of just odd primes, 
aka the number will be odd

Then when we add 1 to that, the number will
end up being even, which is definitely NOT
prime!

2^2+1 = 5 < new prime!
2^1*3^1+1 = 7
2^1*5^1+1 = 11
2^2*3^1+1 = 13

Ok idk why 2^1*7^1+1 isn't prime, but whatever

2^4+1 = 17
2^1*3^2+1 = 19
2^1*11^1+1 = 23
2^2*7^1+1 = 29
2^1*3^1*5^1+1 = 31
2^2*3^2+1 = 37
2^3*5^1+1 = 41
2^1*3^1*7^1+1 = 43
2^1*23^1+1 = 47


there doesn't seem to be a pattern between
multiples of primes plus one that are actually
primes and ones that aren't :(

So the method rn is to generate a bunch of odd
numbers with this method, then check with the
list of already confirmed primes to check
whether the generated numbers are actually prime
or not.

Not the most efficient, but still more efficient
than our previous methods

"""




from factorizerprinter import isPrime


def primeLister3(maxNum):
	# this part generates not necessarily prime numbers
	# but RECUSIVELY!!!! (maybe idk)
	primeNumList = [2]
	womboCombo = 2
	tempComboWombo = 0
	while womboCombo < maxNum:
		# generates least possible womboCombo greater than 
		# previous womboCombo
		while tempComboWombo < womboCombo-1:
			tempComboWombo = primeNumList[0]
			#YOU LEFT OFF HERE
		womboCombo = tempComboWombo+1
		# if the new number generated greater than the
		# previous womboCombo IS actually prime, then
		# append new womboCombo to the prime list
		if isPrime(womboCombo):
			primeNumList.append(womboCombo)



"""

primes minus 1 divided by 2


3 -> 1
5 -> 2
7 -> 3
11 -> 5
13 -> 6
17 -> 8
19 -> 9
23 -> 11
29 -> 14
31 -> 15
37 -> 18
41 -> 20

"""
