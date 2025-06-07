#Q.3 accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.

print("Enter 5 numbers: ")

mylist = []
for i in range(5):
    num1 = int(input())
    mylist.append(num1)
    
print("First List: ", mylist)

print("Enter 3 more numbers: ")

mylist2 = []
for i in range(3):
    num2 = int(input())
    mylist2.append(num2)
    
print("Second List: ", mylist2)

mylist.extend(mylist2)

print("Final List:" ,mylist)
