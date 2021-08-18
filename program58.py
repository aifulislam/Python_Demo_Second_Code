#Magic methods-------------

class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __str__(self):
        return (f"Name : {self.name},Color : {self.color}")
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color
    def display(self):
        print(f"Name : {self.name},Color : {self.color}")

bike1 = bike("Hero","red")
bike2 = bike("Hero","red")
#print(bike1.display())
print(bike1==bike2)
