class   Arithmatic:
    def __init__(self,val):
        self.a = val

    def __add__ (self,other):
        return self.a + other.a
    
    def __sub__ (self,other):
        return self.a - other.a
    
    def __mul__(self, other):
        return self.a * other.a
    
    def __pow__(self, other):
        return self.a ** other.a
    
    def __truediv__(self, other):
        return self.a/other.a
    
    def __floordiv__(self, other):
        return self.a // other.a
    
    def __mod__(self, other):
        return self.a%other.a
    
ob1 = Arithmatic(30)
ob2 = Arithmatic(20)


print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1**ob2)
print(ob1/ob2)
print(ob1//ob2)
print(ob1%ob2)

# It is a magic mathod