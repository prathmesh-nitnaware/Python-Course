#accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  after removing it, display the list.

mylist = []
print("Enter 5 numbers: " ,end=' ')
for i in range(5):
    num = int(input())
    mylist.append(num)

print(mylist)

idx = int(input("Enter index number to remove: "))
mylist.pop(idx)
print(mylist)
