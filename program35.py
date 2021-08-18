##Lambda Functions---------------

def calculate(x,y):
    return x*y + 2*x*y + y*y

#lambda paramater : expression
#print((lambda a,b : a*a + 2*a*b + b*b)(2,3))

print(calculate(2,3))

##Lambda Functions---------------
#lambda paramater : expression
print((lambda a,b : a*a + 2*a*b + b*b)(2,3))

##Lambda Functions---------------

def qube(x):
    return x*x*x

s = ((lambda  x : x*x*x )(4))
print(s)

#Lambda Functions---------------

def add(x,y):
    sum = x+y
    return sum

s = ((lambda x,y : x+y)(10,20))
print(s)
