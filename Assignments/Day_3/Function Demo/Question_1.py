"""Q.1 define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]"""

def add():
    print("This is Add function")

def modify():
    print("This is Modify function")

def delete():
    print("This is Delete function")

num = int(input("Enter a number: "))

match num:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
