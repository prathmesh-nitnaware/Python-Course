"""define a function in such a way that it can accept n number of values and print their sum. 
[ variable number of arguments]"""

def fun(*var):
    sum = 0
    for i in var:
        sum+=i
    print("Sum = ",sum)
fun(2,3,4,4)
fun(1)
fun(50,47)

