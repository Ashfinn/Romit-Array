x = int(input("Enter a number: "))
summation = sum(i for i in range(1, x+1) if x % i == 0)
print('Perfect') if summation/2 == x  else print('Imperfect')
