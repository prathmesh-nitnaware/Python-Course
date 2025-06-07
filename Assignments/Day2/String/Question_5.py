#accept a string and find out how many words are there in it.

stg = input("Enter a string: ")
a = stg.split()

for i in a:
    print(f"'{stg}' has {len(i)} letters")
