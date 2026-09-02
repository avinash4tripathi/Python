class demo:
    name = 'pyhton'

    def greet(self):
        print("good evening")

class Myclass(demo):
    pass
ob1 = Myclass()
ob1.greet() 





class car():
    model = "Fortuner"
    def feature(self):
        print("Legacy")

class Myclass(car):
    pass

obj1 = Myclass()
obj1.feature()