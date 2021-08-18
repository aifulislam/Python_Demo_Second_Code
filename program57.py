#Polymorphism----------
#Bild in Polymorphic function--------
print(len("Ariful Islam"))
print(len([10,20,30,40,50]))

#User Defined Polymorphic function--------
def add(x,y,z=0,t=0):
    return x+y+z+t

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
