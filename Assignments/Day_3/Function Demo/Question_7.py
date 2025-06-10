"""define a function which accepts a string , toggle and return it.
	[ hint :  use "swapcase()" function of striing]"""

def fun(str):
    return str.swapcase()
str = input("Enter a string: ")
x = fun(str)
print(x)
