#List Comprehensions----------

num =[1,2,3,4,5]
#[expression for item in list]
result = [x*x for x in num]
print(result)

#List Comprehensions----------
num =[1,2,3,4,5]
#[expression for item in list]
result=[x for x in num if x%2==0]
print(result)

#List Comprehensions----------

num = [1,2,3,4,5]
result = [x for x in num if x%2!=0]
print(result)

#List Comprehensions----------
num = [1,2,3,4,5]
result=[x*x*x  for x in num]
print(result)

#List Comprehensions----------
num = [1,2,3,4,5,6,7,8,9]
result= [x+x for x in num]
print(result)

#List Comprehensions----------
#map()-----
num = [1,2,3,4,5,6]
#[expresion for item in list]
result = [x*x*x for x in num]
print(result)

#filter()-----
num = [1,2,3,4,5,6]
#[expresion for item in list]
#result = list(filter(lambda x: x%2==0,num))
result = [x for x in num if x%2!=0]

print(result)

