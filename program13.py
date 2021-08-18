#Logical operator--------
#Maximum ----
num1 = 30
num2 = 40
num3 = 50

if num1>num2 and num1> num3:
    print(num1)
if num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

#Vowel ----

ch = "z"
if ch =="a" or ch =="e" or ch=="i" or ch=="o" or ch=="u" or \
        ch =="A" or ch =="E" or ch=="I" or ch=="O" or ch=="U":
    print("Vowel")
else:
    print("Consonant")
