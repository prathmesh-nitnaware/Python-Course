#first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.

mylist =[]
while(True):
    num = int(input("Enter a number: "))
    if num==0:
        break
    else:
        mylist.append(num)
print(mylist)
print(len(mylist))
