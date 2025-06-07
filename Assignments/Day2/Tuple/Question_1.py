#Write a Python program to count the elements in a list until an element is a tuple.

mylist = [10, 20, 'hello', 3.14, [1, 2], (5, 6), 99, 'done']
c = 0
for i in mylist:
    if isinstance(i, tuple):
        break
    c += 1

print("Number of elements before a tuple:", c)
