#Inheritance-----

class phone:
    def call(self):
        print("You can call me.")

    def massege(self):
        print("You can sent messege.")

class samsang(phone):

    def photo(self):
        print("You can take photo.")

p = samsang()
p.call()
p.massege()
p.photo()
print(issubclass(samsang,phone))
