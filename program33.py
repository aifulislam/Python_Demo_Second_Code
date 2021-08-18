#xxargs and xxxargs------------
#xxargs-----------

def student(id,name,gpa):
    print(id,name,gpa)

student(101,"Arif",4.50)


def student(*details):
    print(details[3])

student(101,"Arif",4.50,25)
student(102,"Tamim",4.60,24)


def add(*details):
    sum = 0
    for num in details:
        sum = num + num
        print(sum)

add(10,20)
add(10,20,30)
add(10,20,40,50)

def sub(*details):
    sum = 0
    for num in details:
        sum = sum + num
    return (sum)

s = sub(300,200)
print(s)


#xxxargs-----------
def student(**details):
    print(details)

student(id=101,name="Arif",gpa=4.50)


def teacher(**details):
    print(details)

teacher(id="1010",name="Rofiq",subject="Math")


