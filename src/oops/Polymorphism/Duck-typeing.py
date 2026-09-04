# Diffent class with same method?


class Animal:
    def speak(self):
        print("Animal can spaek")


class Human:
    def speak(self):
        print("Human Can Speak")


class Dog:
    def speak(self):
        print("Dog can Buck....")


class Cat:
    def speak(self):
        print("Cat Meaus...")


ob1 = Animal()
ob2 = Human()
ob3 = Dog()
ob4 = Cat()

ob2.speak()
ob1.speak()
ob3.speak()
