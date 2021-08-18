#Python 51 - Introducing Methods-----------

class Student:
    name = ""
    class1 = ""
    roll = ""
    gpa = ""

#Using setValue Methods---------
    def setValue(self, name, class1, roll, gpa):
        self.name = name
        self.class1 = class1
        self.roll = roll
        self.gpa = gpa

#Using  Display Methods---------
    def display(self):
        print(f"Name : {self.name}, Class : {self.class1}, Roll : {self.roll}, GPA : {self.gpa}")

Arif = Student()
#print(isinstance(Arif,Student))
Arif.setValue("Ariful Islam","MA",101,3.50)
Arif.display()

Tamim = Student()
Tamim.setValue("Tamim Iqbal","BA",102,3.00)
Tamim.display()

Nazim = Student()
Nazim.setValue("Nazim Uddin","MA",103,3.40)
Nazim.display()

