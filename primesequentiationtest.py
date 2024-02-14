#PRIME SEQUENTIAION!

#expressing numbers as the powers of their prime factorization

#2^x1, 3^x2, 5^x3, 7^x3

num = str(input("What is your prime sequentiation? "))

pnum = 2**int(num[3]) * 3**int(num[2]) * 5**int(num[1]) * 7**int(num[0])

print("Your number is: " + str(pnum))