#Python - class and object------
#Using  Display Methods---------
#Using setValue Methods---------
#Constructor----------

class Teacher:
    name = ""
    Id = ""
    gpa = ""
    passed = ""
    year = ""

    def __init__(self,name,Id,gpa,passed,year):
        self.name = name
        self.Id = Id
        self.gpa = gpa
        self.passed = passed
        self.year = year

    def display(self):
        print(f"Name : {self.name}, Id: {self.Id},GPA : {self.gpa}, Passed : {self.passed},Year : {self.year}")

Arif = Teacher("Ariful Islam",101,3.60,"MA",2019)
Arif.display()

Tamim = Teacher("Tamim Iqbal",102,3.50,"BA",2018)
Tamim.display()

Nazim = Teacher("Nazim Uddin",103,3.00,"MA",2017)
Nazim.display()

Nasim = Teacher("Nasim Khan",104,3.40,"MA",2018)
Nasim.display()

