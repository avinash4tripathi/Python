"""class demo:
    def __init__(self,name,address,subject,rollno):
        self.name= name
        self.address = address
        self.subject = subject
        self.rollno = rollno

class Bye(demo):
    def __init__(self, name, adders,subject,rollno,email):
        super().__init__(name, adders,subject,rollno)
        self.email= email

ob1 = Bye('Aviash','Noida','Maths',2205080130016,'tripathiavinash@gmail.com')
print(ob1.name)
print(ob1.email)
print(ob1.subject)
print(ob1.address)
print(ob1.rollno)"""


class main:
    def show(self):
        print("This is main class")

    def greet(self):
        print("hii GoodAfternooon")


class myclass(main):
    def show(self):
        print("This is my class")


ob1 = myclass()
ob1.greet()
ob1.show()
