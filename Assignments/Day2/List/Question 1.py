#Q.1 create a list , accept a number,name and a float value from user and store it inside the list. Now accept one more name from user and insert it at 2nd position. Accept a number and append it at the end of the list.
print the entire list.


mylist = []
name1 = input("Enter your name: ")
mylist.append(name1)
num1 = (float(input("Enter a decimal value : ")))
mylist.append(num1)
name2 = input("Enter name : ")
mylist.insert(2, name2)
num2 = int(input("Enter a number: "))
mylist.append(num2)

print(mylist)
