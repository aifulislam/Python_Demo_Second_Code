#Python - Method Overriding--------

class phone:
    def __init__(self):
        print("I am in phone class")

class samsang(phone):
    def __init__(self):
        super().__init__()
        print("I am in samsang class")

p = phone()
s = samsang()








