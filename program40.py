#45 - Reading a file-----------------

file = open("student.txt","r+")
'''
print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
text = file.readlines()[3]
print(text)
'''
for line in file:
    print(line)
file.close()
