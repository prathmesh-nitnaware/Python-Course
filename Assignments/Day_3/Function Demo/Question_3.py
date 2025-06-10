#define a function which accepts character,int,string and display them.

def fun(val):
    if val.isdigit():
        print("This is an int")
    elif len(val) == 1 and val.isalpha():
        print("This is a character")
    elif isinstance(val, str):
        print("This is a string")
    else:
        print("Error")

a = input("Enter something: ")
fun(a)

print("Done")
