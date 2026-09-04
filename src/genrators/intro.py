def creater():
    list= []
    i = 1
    while i<= 200:
        list.append(i) 
        i += 1  
    return list
print(creater())

print('=='*10)

#So the main probelm in we can not genrate everything at one we genrte it on by one according to our need.
#So we use genrator. 

def creater1():
    i = 1
    while i<= 200:
        yield i
        i += 1
print(creater1())
x = creater1()
print(next(x)) # It genrates one by one not at onces entire list
print(next(x))
print(list(x))

print('=='*10)
 
import sys # this use for we use the system
def creater():
    list= []
    i = 1
    while i<= 200:
        list.append(i)
    return list
print(creater())
z =sys.getsizeof(list) # this is use to find how much space is occupied by the programm
print(z)
print([num+10 for num in creater()])