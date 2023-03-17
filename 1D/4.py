x = input("Enter a number: ")
sum = 0;
for i in range(len(x)):
    sum += int(x[i])
reversed_str = str(sum)
reversed = int(reversed_str[::-1])
if reversed * int(reversed_str) == int(x):
    print ("Harshad")
else:
    print ("Not Harshad")