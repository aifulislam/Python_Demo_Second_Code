#map and filter function----------
#map function-----

def squre(x):
    return x *x

num = [1,2,3,4,5]
result = list(map(squre,num))
print(result)

#map function-----

def qube(x):
    return x*x*x

num = [1,2,3,4,5]
result = list(map(qube,num))
print(result)

#map-----------
def squre(x):
    return x*x
num = [1,2,3,4,5]
result = list(map(squre,num))
print(result)


def qube(x):
    return x*x*x
nam = [9,8,7,6,5]
a = list(map(qube,nam))
print(a)

#filter function----------

num =[1,2,3,4,5]
result = list(filter(lambda x: x%2==0,num))
print(result)

#filter function----------

num = [11,22,33,44,55,66]

result = list(filter(lambda x: x%2!=0,num))
print(result)

#filter--------

num = [1,2,3,4,5,6,7]
result = list(filter(lambda x: x%2==0,num))
print(result)

nam = [1,2,3,4,5,6,7]
a = list(filter(lambda x: x%2!=0,nam))
print(a)
