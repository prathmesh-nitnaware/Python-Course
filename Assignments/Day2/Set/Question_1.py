"""accept 10 values from user and add them inside the set. 
now accept one more value from user and if it is present in the set, remove it. 
Make sure program doesn't give any error if number is not there inside the set."""

myset = set()
print("Enter 10 values:")

for i in range(10):
    num = input(f"Enter {i+1} value: ")
    myset.add(num)

print("Initial Set:", myset)

remove = input("Enter one more value to remove if present: ")

myset.discard(remove)

print("Updated Set:", myset)
