
#Introduction to OOP - class and object-------
class student:
    Roll = ""
    Gpa = ""

Arif = student()
print(isinstance(Arif,student))
Arif.Roll = 101
Arif.Gpa = 4.50
print(f"Roll : {Arif.Roll},Gpa : {Arif.Gpa}")

Tamim = student()
Tamim.Roll = 102
Tamim.Gpa = 4.00
print(f"Roll : {Tamim.Roll},Gpa : {Tamim.Gpa}")

Nasim = student()
Nasim.Roll = 103
Nasim.Gpa = 4.20
print(f"Roll : {Nasim.Roll},Gpa : {Nasim.Gpa}")

