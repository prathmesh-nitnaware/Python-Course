"""Q.8Note: use List comprehension
 create a list with the numbers from 1 to 20
 create one more list which should contain only odd numbers from the first list."""

mylist = []
for i in range(1, 21):
    mylist.append(i)

print(mylist)

oddlist = [i for i in mylist if i % 2 != 0]
print(oddlist)
