"""define a class "Student" with members name,age,address and qualification 
define parameterized constructor and "str" member function which returns all the members
create 4 objects of Student by passing values.
now create a dictionary with rollno ( start from 1 ) as a key and student object as a value.
accept a rollno from user and display all its details i.e. name,age,address and qualification.
also display message "student not found" in case if rollno entered by user is not available as a key inside the dictionary."""


class Student:
    def __init__(self, name, age, address, qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nQualification: {self.qualification}"

s1 = Student("Prathmesh", 20, "Mumbai", "B.Tech")
s2 = Student("Vishal", 20, "Mumbai", "B.Tech")
s3 = Student("Anuj", 22, "Mumbai", "B.Tech")
s4 = Student("Riyan", 23, "Mumbai", "B.Tech")

students = {
    1: s1,
    2: s2,
    3: s3,
    4: s4
}

rollin = input("Enter roll number: ")

if rollin.isdigit():
    i = int(rollin)
    if i in students:
        print("Student Details:")
        print(students[i])
    else:
        print("student not found")
else:
    print("Invalid input. Please enter a number.")
