# Encapsulation is the Phenomena of wraping the data and method in a single unit.

class demo:
    __a = 10
    b = 20

    def __init__(self):
        __name = "Mr.X"
    
    def info(self):
        print("This is Demo Class")

    def __password(self):
        print("x@123")

    def prop1(self):
        print(self.__a)
    
ob1 = demo()
print(ob1.b)
ob1.prop1()