#set Data Structure ------------

num1 = {1,2,3,4,5,5}
num2 = set([4,5,6])
num2.add(8)
num2.remove(5)

print(7 in num1)
print(7 not in num2)

#set : Union -------

num1 = {1,2,3,4,5,6,7}
num2 = set([5,6,7,8,9])

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)

#set : Union -------

num1 = {1,2,3,4,5,6,7,8}
num2 = {5,6,7,8,9,10}
num3 = set({6,7,8,11,12,13,14})
num1.add(6)
num1.remove(6)
print(num1)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)

print(num2 | num3)
print(num2 & num3)
print(num2 - num3)

#set Data Structure -----------

num1 = {10,20,30,40,50}
num2 = set([30,40,50,90,100])
num2.add(11)
num2.remove(90)
print(90 not in num2)
print(33 in num1)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)


