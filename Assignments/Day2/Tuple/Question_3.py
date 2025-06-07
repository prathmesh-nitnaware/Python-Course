#Write a Python program to find the repeated items of a tuple.

tuple = (30, 49, 5, 12, 100, 5 , 19, 2)

repeat = set([item for item in tuple if tuple.count(item) > 1])
print("Repeated items:", repeat)
