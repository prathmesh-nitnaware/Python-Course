#Q.5 accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list
#and  after removing it, display the list.

mylist = []
print("Enter 5 numbers: " ,end=' ')
for i in range(5):
    num = int(input())
    mylist.append(num)

print(mylist)

num = int(input("Enter a number to remove: "))
mylist.remove(num)

print(mylist)
