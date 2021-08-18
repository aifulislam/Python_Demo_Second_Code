#List as input from user--------

n = input("Enter a text or number : ")
#10 20 30 40 50 = sum ?
list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)
print(sum)

#List as input from user--------

n = input("Enter a text or number : ")
print(n)
list = n.split()
sum = 0

for x in list:
    sum = sum + int(x)
print(sum)

#List as input from user--------

n = input("Enter any text or number : ")
print("Numbers are : ",n)
list = n.split()
sum = 0

for num in list:
    sum =  sum + int(num)
print("Sum : ",sum)


#List as input from user--------

numOfDigits = 0
numOfLetters = 0
numOfWords = 0
text = input("Enter a text or numbers : ")

for x in text:
    if x>= "a" and x<="z":
        x = x.lower()
        numOfLetters = numOfLetters + 1
    elif x>="0" and x<="9":
        numOfDigits = numOfDigits + 1
    elif x == " " :
        numOfWords = numOfWords + 1

print("numOfLetters : ",numOfLetters)
print("numOfDigits : ",numOfDigits)
print("numOfWords : ",numOfWords + 1)


#List as input from user--------

numOfDigits = 0
numOfLetters = 0
numOfWords = 0
text = input("Enter a text or number : ")
for x in text:
    x = x.lower()
    if x>="a" and x<="z":
        numOfLetters = numOfLetters + 1
    elif x>="0" and x<="9":
        numOfDigits = numOfDigits + 1
    elif x==" ":
        numOfWords = numOfWords + 1

print("numOfLetters : ",numOfLetters)
print("numOfDigits : ",numOfDigits)
print("numOfWords : ",numOfWords + 1)

