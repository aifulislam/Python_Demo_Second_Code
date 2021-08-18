#https://pynative.com/
print('My', 'Name', 'Is', 'James', sep='**')
print('my' , 'name' ,'is', 'arif' ,sep='##')
print('%o,' % (8))
print('%o,' % (16))
print('%.2f' % 458.541315)
print('%2f' % 543.56456)

floatNumbers = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("User List is ", floatNumbers)

for i in range(10, 15, 1):
  print( i, end=', ')

var = "James" * 2  * 3
print(var)
x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)

hh= 5**2
kk = 5**3
print(hh)
print(kk)

salary = 8000

def printSalary():
    salary = 12000
    print("Salary:", salary)

printSalary()
print("Salary:", salary)

var= "James Bond"
print(var[2::-1])
hh = "ariful islam"
print(hh[4::-1])

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )

p, q, r = 10, 20 ,30
print(p, q, r)
for x in range(1,5,1):
    print(x)

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )


sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add("jjh")
print(sampleSet)

var1 = 1
var2 = 2
var3 = 3

print(var1 + var2 + var3)

str = "pynative"
print (str[1:3])

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

