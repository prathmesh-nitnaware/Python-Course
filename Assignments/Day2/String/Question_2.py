#accept a string and display it. now accept slicing positions from and to , slice the string and display it.

stg = str(input("Enter a string: "))
idx1 = int(input("Enter index number to remove from: "))
idx2 = int(input("Enter index number to remove to: "))

stg2 = stg[:idx1-1] + stg[idx2:]
print("The String ", stg2)
