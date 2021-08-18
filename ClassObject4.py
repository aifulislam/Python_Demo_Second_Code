
#Exercise------

#Triangle----
class triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def areaOfTriangle(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle : ",area)

t1 = triangle(10,20)
t1.areaOfTriangle()

t2 = triangle(20,20)
t2.areaOfTriangle()

#Rectangle-----
class Rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def areaOfRectangle(self):
        area = self.base * self.height
        print("Area of Rectangle : ",area)

r1 = Rectangle(10,20)
r1.areaOfRectangle()

r2 = Rectangle(20,20)
r2.areaOfRectangle()

#Sercle-----
class sercle:
    def __init__(self,radius):
        self.radius = radius

    def areaOfSercle(self):
        area = 3.1416 * self.radius * self.radius
        print("Area of Sercle : ",area)

r1 = sercle(2)
r1.areaOfSercle()

r2 = sercle(3)
r2.areaOfSercle()

