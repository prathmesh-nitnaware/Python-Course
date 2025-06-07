#accept a string and display whether it is palindrom or not.

stg = str(input("Enter a string: "))

rev = stg[::-1]
print("Reversed String: ", rev)

if stg ==rev:
    print(f"The String {stg} is Palindrome!")
else:
    print(f"The String {stg} is not Palindrome!")
