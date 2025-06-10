#define a function which accepts a character and return toggle of it

def fun(char):
    char = char.swapcase()
    return char

char =  input("Enter a character: ")
x = fun(char)
print(x)
