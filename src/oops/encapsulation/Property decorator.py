class Person:
    def __init__(self, age):
        self.age = age

    @property  # getter method
    def show_age(self):
        print(self.age)

    @show_age.setter  # ye mera setter ka proerty decorator hai
    def show_age(self, new):  # setter method
        self.age = new

    @show_age.deleter  # ye mera setter ka property decorator hai
    def show_age(self):
        del self.age


ob1 = Person(20)
ob1.age
ob1.show_age
ob1.show_age = 25
ob1.show_age
print("Deleting the property")
del ob1.show_age


# Q.Example of this method ,ksise bhi methos ko proprty bana sakte hai with the help of propertY decorator


class Bank:
    def __init__(self, bal):
        self.__bal = bal

    @property  # method ko property jaise bannne ke liye property decoratore use karte hai aur ye decorator user friendly hota
    def bal(self):
        print(self.__bal)


ob1 = Bank(1000)
ob1.bal
