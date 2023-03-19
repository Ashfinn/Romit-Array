x = input("Enter a number: ")
print("Palindrome") if int(x[::-1]) == int(x) else print("Not a palindrome")
