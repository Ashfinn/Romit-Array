x = input("Enter a number: ")
reversed = int(x[::-1])
if reversed == int(x):
    print("Palindrome")
else:
    print("Not a palindrome")
