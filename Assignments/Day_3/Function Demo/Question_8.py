"""write a function to accept minimum 3 characters and maximum 5 characters. 
 	[ use default arguments method ]"""

def func(char1,char2,char3,char4='x',char5='y'):
    print("char1 : ",char1,end=' ')
    print("char2 : ",char2,end=' ')
    print("char3 : ",char3,end=' ')
    print("char4 : ",char4,end=' ')
    print("char5 : ",char5,end=' ')
    print()
func('a','b','c')
func('a','b','c','d')
func('a','b','c','d','e')

