#Inheritance-----------
#Parent, Super ,Base Class--
#Child, Sub, Drived Class----

class phone:
    def call(self):
        print("You can call")
    def massage(self):
        print("You can message")

class samsang(phone):
    def photo(self):
        print("Take photos")

p = samsang()
p.call()
p.massage()
p.photo()
print(issubclass(samsang,phone))

#Inheritance-----------

class Teacher:
    def __init__(self,name,passed,gpa):
        self.name = name
        self.passed = passed
        self.gpa = gpa

    def display(self):
        print(f"Name : {self.name},SSC Passed : {self.passed},Gpa : {self.gpa}")

class Student(Teacher):
    def __init__(self,name,passed,gpa,class1,roll):
        #samsang.__init__()
        self.name = name
        self.passed = passed
        self.gpa = gpa
        self.class1 = class1
        self.roll = roll

    def display(self):
        print(f"Name : {self.name},SSC Passed : {self.passed},Gpa : {self.gpa},Class : {self.class1},Roll : {self.roll}")

print("Teacher Details : ")
Arif = Teacher("Ariful Islam",2015,4.50)
Arif.display()

Tamim = Teacher("Tamim Iqbal",2016,4.00)
Tamim.display()

Nazim = Teacher("Nazim Uddin",2017,4.20)
Nazim.display()

Nasim = Teacher("Nasim Khan",2015,4.30)
Nasim.display()

print(issubclass(Student,Teacher))
print("Student details : ")
Nazim = Student("Nazim Uddin",2017,4.20,"One",101)
Nazim.display()

Nasim = Student("Nasim Khan",2015,4.30,"Two",102)
Nasim.display()

