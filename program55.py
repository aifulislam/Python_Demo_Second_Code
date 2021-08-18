#Types Of Inheritance----------
#Multi-level inheritance------

class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    def display2(self):
        print("I am inside B class")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")

ob1 = C()
ob1.display3()

#Multi-level inheritance------

class A:
    def student1(self):
        print("I am a student1")

class B(A):
    def student2(self):
        print("I am a student2")

class C(B):
    def student3(self):
        super().student1()
        super().student2()
        print("I am a student3")

s = C()
s.student3()

#Types Of Inheritance----------
#Multiple inheritance------

class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(B,A):
    pass

ob1 = B()
ob1.display()

#Types Of Inheritance----------
#Multi-level inheritance------

class A:
    def Student1(self):
        print("I am A class")

class B(A):
    def Student2(self):
        print("I am B class")

class C(B):
    def Student3(self):
        super().Student1()
        super().Student2()
        print("I am C class")

ob1 = C()
ob1.Student3()

#Multiple inheritance------

class A:
    def Student(self):
        print("I am A class")

class B:
    def Student(self):
        print("I am B class")

class C(B,A):
    pass

ob1 = C()
ob1.Student()

