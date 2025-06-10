#define a function which accepts a number and return its square

def square(x):
    return x**2

num = int(input("Enter a number: "))
a = square(num)
print(f"The Square of {num} is {a}")
