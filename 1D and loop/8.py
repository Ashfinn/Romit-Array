from math import factorial
try:
    print('''
    1. nCr
    2. nPr
    ''')
    x = input()
    def nCr():
        n = int(input("n = ?: "))
        r = int(input("r = ?: "))
        nCr = factorial(n)/(factorial(n-1)*factorial(r))
        print (nCr)
    def nPr():
        n = int(input("n = ?: "))
        r = int(input("r = ?: "))
        nPr = factorial(n)/factorial(n-r)
        print (nPr)
    if x == "1":
        nCr()
    elif x == "2":
        nPr()
    else:
        print ("Invalid input")
except ValueError:
    print ("r should be less than n and both should be positive")