#Python 50 - Introduction to OOP - class and object------

class Student:
    class1 = ""
    roll = ""
    gpa = ""

Arif = Student()
#print(isinstance(Arif,Student))
Arif.class1 = "MA"
Arif.roll = 101
Arif.gpa = 3.50
print(f"Class : {Arif.class1},Roll : {Arif.roll},GPA : {Arif.gpa}")

Tamim = Student()
Tamim.class1 = "BA"
Tamim.roll = 102
Tamim.gpa = 3.00
print(f"Class : {Tamim.class1},Roll : {Tamim.roll},GPA : {Tamim.gpa}")

#Python 50 - Introduction to OOP - class and object------

class Teacher:
    name = ""
    Id = ""
    passed = ""

Arif = Teacher()
#print(isinstance(Arif,Teacher))
Arif.name = "Ariful Islam"
Arif.Id = 101
Arif.passed = "MA"
print(f"Name : {Arif.name},ID : {Arif.Id},Passed : {Arif.passed}")

Tamim = Teacher()
Tamim.name = "Tamim Iqbal"
Tamim.Id = 102
Tamim.passed = "BA"
print(f"Name : {Tamim.name}, ID : {Tamim.Id}, Passed : {Tamim.passed}")

Nazim = Teacher()
Nazim.name = "Nazim Uddin"
Nazim.Id = 103
Nazim.passed = "MA"
print(f"Name : {Nazim.name}, ID : {Nazim.Id}, Passed : {Nazim.passed}")

