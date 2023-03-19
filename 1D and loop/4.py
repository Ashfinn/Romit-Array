x = input("Enter a number: ")
summation = str(sum(int(i) for i in x))
reversed = int(summation[::-1])
print ("Harshad") if reversed * int(summation) == int(x) else print ("Not Harshad")