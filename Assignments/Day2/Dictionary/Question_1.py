#accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.

stud = {}
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    stud[i] = name

print("Student Dictionary: " ,stud)
