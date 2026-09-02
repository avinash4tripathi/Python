class GraminBank:
    def __init__(self,name,adders):
        self.name = name
        self.addres = adders
class SBI(GraminBank):
    def __init__(self, name, adders,email):
        super().__init__(name, adders)
        self.email= email 
    
C1 = SBI('Abhisek','jaipur','Abhi@gmail.com')
C2 = GraminBank('Avi','nopida','Avin')

print(C1.name)
print(C1.addres)
print(C1.email)
print(C2.name) 
        


class demo:
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
print(ob1.rollno)