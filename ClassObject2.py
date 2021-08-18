
#Introduction to OOP - class and object-------
#Introducing Methods----------

class student:
    Roll = ""
    Gpa = ""

    #Methods--
    def setValue(self,Roll,Gpa):
        self.Roll = Roll
        self.Gpa = Gpa

    def display(self):
        print(f"Roll : {self.Roll},Gpa : {self.Gpa}")


Arif = student()
Arif.setValue(101,4.50)
Arif.display()

Tamim = student()
Tamim.setValue(102,4.20)
Tamim.display()

Nasim = student()
Nasim.setValue(103,4.00)
Nasim.display()

