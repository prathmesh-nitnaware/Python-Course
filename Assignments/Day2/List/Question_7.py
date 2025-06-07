"""Create a list and store string,number,character,boolean,decimal values respectively inside it.
Now slice it in following ways:
a) display it in reverse order
b) list all the elements from 2nd position
c) list the elements from 1st to 3rd position
d) slice it from 1st to 3rd elements from the end."""

mylist = []
stg = str(input("Enter a string: "))
mylist.append(stg)
num = int(input("Enter a number: "))
mylist.append(num)
char = input("Enter only one character: ")
mylist.append(char)
boln = bool(input("Is this a bolen? (Y/N): "))
mylist.append(boln)
dec = float(input("Enter a decimal number: "))
mylist.append(dec)

print("List Created: " ,mylist)

#a)Printing in Reverse Order
print("Reverse of the List: ",mylist[::-1])

#b) printing element at 2nd position
print("Element at 2nd Position: " ,mylist[2])

#C)Displaying 1st and 3rd element
print("Displaying 1st and 3rd elements: " ,mylist[1:4:2])

#D) Slice it from 1st to 3rd element from the end
print("Slicing from 1st to 3rd element from the end: ", mylist[-3:])
