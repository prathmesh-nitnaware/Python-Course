"""Given a dictionary of students and their favourite colours: 
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
1. Find out how many students are in the list 
2. Change Lisa’s favourite colour 
3. Remove 'Jenny' and her favourite color
4. Sort and print students and their favourite colours alphabetically by name"""

stud = {
    'Arham': 'Blue',
    'Lisa': 'Yellow',
    'Vinod': 'Purple',
    'Jenny': 'Pink'
}

print("Student Details:" ,stud)

# 1. Find number of students
print("Total students:", len(stud))

# 2. Change Lisa’s favourite colour
stud['Lisa'] = 'Green'

# 3. Remove 'Jenny' and her favourite color
del stud['Jenny']

# 4. Sort and print students and their favourite colours alphabetically by name
for name in sorted(stud):
    print(name, ":", stud[name])


print("\nDone")
