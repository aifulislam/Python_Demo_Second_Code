#Python 52 - Constructor----------

class Student:
    name = ""
    class1 = ""
    roll = ""
    gpa = ""

#Using Constructor-----
    def __init__(self, name, class1, roll, gpa):
        self.name = name
        self.class1 = class1
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name : {self.name}, Class : {self.class1}, Roll : {self.roll}, GPA : {self.gpa}")

Arif = Student("Ariful Islam","MA",101,3.50)
Arif.display()

Tamim = Student("Tamim Iqbal","BA",102,3.00)
Tamim.display()

Nazim = Student("Nazim Uddin","MA",103,3.40)
Nazim.display()

