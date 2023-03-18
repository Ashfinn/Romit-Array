from math import *
try:
    print(
'''
1. nCr
2. nPr
'''
    x = input()
    def 
    n = int(input("n = ?: "))
    r = int(input("r = ?: "))

    nCr = factorial(n)/(factorial(n-1)*factorial(r))
    print (nCr)
    nPr = factorial(n)/factorial(n-r)
    print (nCr)
except ValueError:
    print ("r should be less than n")