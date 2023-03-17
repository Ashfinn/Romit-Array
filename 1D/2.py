x = input("Enter a number: ")
sum = 0;
for i in range(len(x)):
    sum +=pow(int(x[i]),3)
if sum == int(x):
    print("Armstrong")
else:
    print("Alienstrong")

