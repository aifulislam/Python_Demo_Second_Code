#Ternary Operator------

num1 = 30
num2 = 40
'''
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
max = (num1 if num1>num2 else num2)
print("Maximum : ",max)
min = (num1 if num1<num2 else num2)
print("Minimum : ",min)
