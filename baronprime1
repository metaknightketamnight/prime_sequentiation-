'''def PrimeList(num) :

	
	returns base-10 list of all unique primes 
	(ie. 4, 8, 16 etc. would all return a list of [2])
	parameter:num=int
	return:primes=list
	

	[]
	return primes


def baseTenToPrimeDict(num) :
	# returns dictionary with keys as primes and values as power
	'''
 # Function imports

def get_factor_list(int_flist) :
    #VER 1
    factors = []
    for i in range(1,int_flist) :
        if (int_flist % i) == 0 :
            factors.append(i)
    factors.append(int_flist)
    return factors
'''
#test :
int_flist = int(input())
print(get_factor_list(int_flist))
'''
def is_prime(int_primebool) :
    # inputs integer, outputs whether or not its a prime
    extinction = True
    for i in range(2, int_primebool) :
        if (int_primebool % i) != 0 :
            continue
        else :  
            extinction = False # THE PRIMES ARE ALIVE, THEY ARE NOT EXTINCT!
            break
    else :
        extinction = True
    return extinction
    
def altimus(cc) : 
    # optimus but (hopefully) better...
    # need is_prime() and get_factor_list()
    # returns list of prime factors 
    altilist = []
    for i in range(cc) :
        if is_prime(i) is True and i in get_factor_list(cc) :
            altilist.append(i)
    if is_prime(cc) == True :
        altilist.append(cc)
    return altilist

'''

def dalti_count(int_kist) :
    daltidict = {}
    for i in range(2, int_kist) :
        if is_prime(i) is True and i in get_factor_list(int_kist) :
            if not int_kist in daltidict :
                daltidict[int_kist] == 1
            elif int_kist in daltidict :
                daltidict[int_kist] += 1
    return daltidict
'''        
            

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# MAIN CODE

    # turn user integers into primes ...
user_input = int(input('Input Number :'))
print(f'{user_input} has {len(altimus(user_input))} primes, {altimus(user_input)}')
if is_prime(user_input) == True :
    print(f'{user_input} has factors 1 and itself, {get_factor_list(user_input)}, and it is a prime number.')
else :
    print(f'{user_input} has factors {get_factor_list(user_input)}, and it is not prime number.')

'''
NOTES :
 - more branches on main code to account for if input is a prime number
'''
