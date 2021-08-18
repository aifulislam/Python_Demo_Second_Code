#Dictionaries----------

studentId = {
    "101" : "Ariful Islam",
    "102" : "Anisul Islam",
    "104" : "Nasim Khan",
    "105" : "Nazim Khan",
    "106" : "Ayon Khan",
    "107" : "Tami Khan",
}
print(studentId["104"])
print(studentId.get("109","Not a valid"))

#Dictionaries----------

studentId = {
    "Arif" : "Ariful Islam" " 24 year old",
    "Anis" : "Anisul Islam",
    "Nasim" : "Nasim Khan",
    "Nazim" : "Nazim Khan",
    "Ayon" : "Ayon Khan",
    "Tamim" : "Tamim Khan",
}
print(studentId["Arif"])
print(studentId.get("rahim","Not a valid"))

#Dictionaries----------
n = int(input("Enter your number : "))

studentId = {
    2020 : "Ariful Islam" " 24 year old",
    2030 : "Anisul Islam",
    2040 : "Nasim Khan",
    2050 : "Nazim Khan",
    2060 : "Ayon Khan",
    2070 : "Tamim Khan",
}

print(studentId.get(n,"Not a valid"))

#Dictionaries----------

studentId = {
    "1010" : "Arif",
    "1020" : "Tamim",
    "1030" : "Nasim",
    "1040" : "Nasim",
    "1050" : "Nahid",
}
print(studentId["1050"])
print(studentId.get("1070","Not a valid"))

