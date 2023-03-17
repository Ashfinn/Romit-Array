x = int(input("Enter a number: "))
i = 1
sum = 0
while i <= x:    
    if x % i == 0:
        sum += i
    i += 1

if sum / 2 == x:
    print("Perfect")
elif sum/2 != x:
    print("Imperfect")