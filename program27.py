#Matrix----------

matrix = [
    [1,2,3],
    [4,5,6]
]
print(matrix[0][2])

matrix = [
    [1,2,3],
    [4,5,6]
]
#value change-----
matrix[0][2]="7"
print(matrix[0][2])

matrix = [
    ["Arif","Tamim","Nazim"],
    ["Ayon","Rajon","Nahid"]
]
matrix[1][2] = "Nasim"
print(matrix[1][2])

#Matrix----------

matrix = [
    [1,2,3],
    [4,5,6]
]
for row in matrix:
    for col in row:
        print(col)


# Matrix----------

matrix = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["L", "M", "N", "O", "P"],
    ["Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z"],
]
print(matrix[2][4])
matrix[1][4] = "K"
for row in matrix:
    for col in row:
        print(col)


#matrix------
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
]

matrix[0][2]= 9
for row in matrix:
    for col in row:
        print(col)
