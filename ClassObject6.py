
#Method Overriding-----------

class phone:
    def __init__(self):
        print("I am in Phone Class")

class Samsang(phone):
    def __init__(self):
        super().__init__()
        print("I am in Samsang Class")


s = Samsang()

