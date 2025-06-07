#A pangram is a sentence that contains all the alphabets.
#example: The quick brown fox jumps over the lazy dog. 
#Your task here is to write a function to check a sentence to see if it is a pangram or not.

def pang(sent):
    sent = sent.lower()
    a = set('abcdefghijklmnopqrstuvwxyz')
    return a.issubset(set(sent))

b = input("Enter a sentence: ")

if pang(b): 
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
