#accept a string and display the characters which are repeated in the string

stg = input("Enter a string: ")
repeat = []

for ch in stg:
    if stg.count(ch) > 1 and ch not in repeat:
        repeat.append(ch)

print("Repeated characters:", repeat)
