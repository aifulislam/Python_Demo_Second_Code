#Stack And Queue---------
#Stack ----

books = []
books.append("Learn C")
books.append("Learn Java")
books.append("Learn Python")
print(books)
books.pop()
print("Now the top books is : ",books[-1])

books.pop()
print("Now the top books is : ",books[-1])

books.pop()
if not books:
    print("No Book left")

#Stack And Queue---------
#Stack ----

student = []
student.append("Learn C")
student.append("Learn C++")
student.append("Learn C#")
student.append("Learn Pyhon")
print(student)
student.pop()
print(student)


student.pop()
print("Now the top student.",student[-1])

student.pop()
print("Now the top student.",student[-1])

student.pop()
if not student:
    print("Not student left.")


#Stack ----

student = []
student.append("Ariful Islam")
student.append("Nazim Uddin")
student.append("Tamim Iqbal")
student.append("Nahid Hasan")

print(student)
student.pop()
print("Now the top Student is : ",student[-1])

student.pop()
print("Now the top Student is : ",student[-1])

student.pop()
print("Now the top Student is : ",student[-1])

student.pop()
if not student:
    print("No student left. ")

#Stack And Queue---------
#Queue ----
from collections import deque

bank = deque(["Arif","Tamim","Nasim"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No person left")

#Stack And Queue---------
#Queue ----
from collections import deque
student = deque(["Arif","Tamim","Nahid"])
print(student)
student.popleft()
print(student)
student.popleft()
print(student)
student.popleft()
print(student)
if not student:
    print("No Student left.")

#Stack And Queue---------
#Stack ----

from collections import deque
student = deque(["Arif","Tamim","Nasim","Nadim"])
print(student)
student.popleft()
print(student)

student.popleft()
print(student)

student.popleft()
print(student)

student.popleft()
print(student)

if not student:
    print("Have no item here")

