#Introduction to Function------------
# Function are two kinds : 1. Library and 2. User Defined Function ----

def add(x,y):
    sum = x + y
    print(sum)

def add2(x,y,z):
    sum = x + y + z
    print(sum)

def sub(a,b):
    sum = a - b
    print(sum)

def mul(x,y):
    sum = x * y
    print(sum)

def div(a,b):
    sum = a / b
    print(sum)

def message():
    print("No parameter")


add(10,20)
add2(10,20,30)
sub(30,20)
mul(10,10)
div(300,20)
message()

def arif(x,y):
    sum = x + y
    return sum

#Returning Value from function-----

def rom(x,y):
    if x > y:
        return x
    else:
        return y

def mom(x,y):
    if x < y:
        return x
    else:
        return y


result = arif(10,20)
print("Result : ",result)

result = rom(40,50)
print("Large : ",result)

result = mom(30,40)
print("Small : ",result)

def moon(x,y):
    sum = x + y
    print(sum)

moon(40,50)

#Returning Value from function-----

def tomp(x,y):
    sum = x / y
    return sum

r = tomp(60,20)
print(r)


def large(x,y):
    if x > y:
        return x
    else:
        return y

r = large(50,70)
print(r)



