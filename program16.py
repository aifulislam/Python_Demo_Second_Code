#Sum of n numbers--------------

sum = 0
i = 1
while i <=20:
    sum = sum + i
    i = i + 1
print("Sum : ",sum)

#Even-------------
sum = 0
l = 2
while l<= 20:
    sum = sum + l
    l = l + 2
print("Even Sum : ",sum)

#Odd-------------
sum = 1
j = 1
while j <= 20:
    sum = sum + j
    j = j + 2
print("Odd Sum : ",sum)

#Input-----------------
n = int(input("Enter last number : "))
sum = 0
i = 1
while i <=n:
    sum = sum + i
    i = i + 1
print("Sum : ",sum)

#Input Even-------------
n = int(input("Enter last Even number : "))
sum = 0
l =  2
while l <= n:
    sum = sum + l
    l = l + 2
print("Even Sum : ",sum)

#Input Odd-------------
n = int(input("Enter last odd number : "))
sum = 0
j = 1
while j <= n:
    sum = sum + j
    j = j + 2
print("Odd sum : ",sum)

