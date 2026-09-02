class Father: 
    def house(self): 
        print("Father's house") 
class Mother: 
    def car(self): 
     print("Mother's car") 
class Child(Father, Mother): 
    pass 

c = Child() 
c.house() 
c.car()