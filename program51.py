#Python - Exercise--01------

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area =0.5 * self.base * self.height
        print("Area of triangle : ",area)

#object-----
t1 = Triangle(10,20)
t1.calculate_area()

t2 = Triangle(20,30)
t2.calculate_area()

#Python - Exercise--02------
#addiction -----
class addiction:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def calculate(self):
        add = self.num1 + self.num2
        print("Addiction : ",add)

a = addiction(10,20)
a.calculate()

b = addiction(30,20)
b.calculate()

#Python - Exercise--03------
#squre -----
class squre:

    def __init__(self,num):
        self.num = num

    def calculate(self):
        #Important part-----
        add = self.num * self.num * self.num
        print("Addiction : ",add)

a = squre(2)
a.calculate()

b = squre(3)
b.calculate()

#Python - Exercise--04------
#Pi -----

class Pi:

    def __init__(self,num):
        self.num = num

    def calculate(self):
        #Important part-----
        add = 3.1416 * self.num * self.num
        print("PI : ",add)

a = Pi(2)
a.calculate()

b = Pi(3)
b.calculate()

#Python - Exercise--05------
#circle and peramiter -----

class circle:

    def __init__(self,r):
        self.radius = r

    def calculate(self):
        #Important part-----
        add = self.radius **2*3.14
        print("Circel : ",add)

    def perimeter(self):
        ara = self.radius *2 *3.14
        print("Perrimeter : ",ara)

newCircle = circle(8)
newCircle.calculate()

newCircle.perimeter()

