'''if 10 > 5
    print("Greater")'''

#Here colon is missing so it shows error so this is error in python and its is a syntax error
# It cannot be handled using try and except in the same code because python must first sucessfully parse the program.

# Run time error:A runtime error occurs while the program is executing. In Python, these situations are generally represented by exceptions.
number = 10
result = number / 0

#o/p:ZeroDivisionError: division by zero

# this is handel by using the :
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")