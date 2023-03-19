x = input("Enter a number: ")
print("Armstrong") if sum(int(digit)**3 for digit in x) == int(x) else print("Alienstrong")