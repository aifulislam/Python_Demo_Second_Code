#A practical example of inheritance--------
#Triangle,Rectangle---------------
#Types Of Inheritance----------
#Hierchical inheritance------

class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method in shape class : ")

class Triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("I am area method in shape class : ",area)

class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("I am area method in shape class : ", area)


t1 = Triangle(20,10)
t1.area()

t2 = Rectangle(20,10)
t2.area()
