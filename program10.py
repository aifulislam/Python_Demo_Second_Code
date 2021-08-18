#if, else statement (practical)-----------
#Pass/Fail---------
mark = 22

if mark >= 33:
    print("Pass")
else:
    print("Fail")

#Large---------------

num1 = 40
num2 = 30
if num1 > num2:
    print("Large number : ",num1)
else:
    print("Large number : ",num2)

#Even/Odd----------

num = 9
if num%2==0:
    print("Even")
else:
    print("Odd")

#Grading------

marks = 33
if marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks>=50:
    print("B")
elif marks>=40:
    print("C")
elif marks>=33:
    print("D")
else:
    print("Fail")
