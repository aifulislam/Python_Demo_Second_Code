#Introduction to OOP - class and object-------
#Introducing Methods----------
#Constructor--------

class student:
    Roll = ""
    Gpa = ""

    #Introducing Methods--
    #Constructor------
    def __init__(self,Roll,Gpa):
        self.Roll = Roll
        self.Gpa = Gpa

    def display(self):
        print(f"Roll : {self.Roll},Gpa : {self.Gpa}")


Arif = student(101,4.50)
Arif.display()

Tamim = student(102,4.20)
Tamim.display()

Nasim = student(103,4.00)
Nasim.display()

