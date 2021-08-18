#Zip Function--------

roll = [101,102,103,104,105]
name = ["Arif","Nahid","Nasim","Nazim","Tamim"]

result = list(zip(roll,name))
print(result)

#Zip Function--------

id = [1010,1020,1030,1040,1050]
name = ["Arif","Nahid","Nasim","Nazim","Tamim"]

result = list(zip(id,name,"ABCDE"))
print(result)

#Zip Function--------

roll = [101,102,103,104,105]
name = ["Arif","Tamim","Rajon","Nahid","Ayon"]

#result = list(zip(name,roll))
print(list(zip("12345",name,roll,"ABCDE")))
