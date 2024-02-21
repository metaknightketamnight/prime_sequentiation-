from prime_finders import brutePrimesHard as fPrimes
from math import sqrt as sq
from math import ceil as ce

def pFac_I(p0) :
	"""
	input a string and output prime sequentiated equivalent
	:parameter(s); p0/'int'
	:return; pF/'str'

	# notes : what would be the benefits/drawbacks of defining fPrimes as a list and then modifying it for the program?
	"""
	max0 = ce(sq(p0))
	dict0 = {}
	pF = ''

	while p0 != 1 :
		for potPrime in fPrimes(max0) :
			if p0 % potPrime != 0 and not(potPrime in dict0) :
				dict0[potPrime] = 0
				print(f'{potPrime} is a new nonfactor')
				# IS NEVER A FACTOR, CEMENT DICT
				continue
			elif p0 % potPrime != 0 and potPrime in dict0 :
				print(f'{potPrime} is not a new nonfactor')
				continue
				# IS NEVER A FACTOR, BUT DO NOT CHANGE DICT
			else :
				assert p0 % potPrime == 0
				print(f'{potPrime} is a new factor')
				# IS A FACTOR

				if potPrime in dict0.keys() :
					dict0[potPrime] += 1
					print(f'{potPrime} is a factor we already have')
				else :
					dict0[potPrime] = 1
					print(f'{potPrime} occurs for the first time')

				p0 //= potPrime 
				print(f'p0: {p0}')
				max0 = ce(sq(p0))
				break
		else : 
			if dict0[p0] in dict0.keys() :
				dict0[p0] += 1
			else :
				dict0[p0] = 1
			break

	print(dict0)

	# not very eloquent, but it'll do!

	for prime, freq in dict0.items() :
		pF += str(freq)

	return pF
		


class primeSeq :

	pS = -1

	def __init__(self, pS) :
		self.pS = pFac_I(int(pS))
		# WORK ON NAMING CONVENTIONS
"""
SEQed = primeSeq(input())

print('SEQed ',SEQed)
print('User pS ',SEQed.pS)
print('Class pS ',primeSeq.pS)
"""

print(pFac_I(50))