#w3resource.com

import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%y-%m-%d"))

from math import pi
r = float(input("Import the radius of the circle : "))
print("The area of circle" + str(r) + "is" + str(pi* r **2))

fname = input("Input first name : ")
lname = input("Input last name : ")
print("Hello "+ fname + " "+lname)

values = input("Input some coma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

filename = input("Input theFile Name : ")
f_extns = filename.split(".")
print("The extention of file is "+repr(f_extns[-1]))

color_list = ["Red","Green","White","Black"]
print("%s %s"%(color_list[0],color_list[-2]))

exam_st_date = (2,3,2000)
print("The examination will start from : %i/%i/%i"%exam_st_date)

a = int(input("Input an integer : "))
n1 = int("%s"%a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print("Sum of all : ",n1 + n2 + n3)

print(abs.__doc__)

import calendar
y = int(input("Input the year : "))
m = int(input("Input the months : "))
print(calendar.month(y,m))

print('''I am Ariful Islam. I am from Bangladesh.........I am a student.
I study.......... BSC in Computer Science in IUBT Dhaka.''')

from datetime import date
f_date = date(2020,8,9)
l_date = date(2020,3,25)
delta = f_date - l_date
print(delta.days)

pi = 3.1416
r = 6.0
v = 4.0/3.0 * pi * r ** 3
print("The volume of the sphere is : ",v)

#Math - trapezoid----

base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid : "))
#base_1 = float(input('Base one value: '))
#base_2 = float(input('Base two value: '))
area = ((base_1 + base_2)/2) * height
print(area)

