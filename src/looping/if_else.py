"""#WAP to check the no is having 4 digit.
a = int(input("enter the number:"))
if a >= 1000 and a<= 999:
    print("the number have 4 digit")
else:
    print("the numbet has not 4 digit ")"""

# WAP to check the whethet the numeber is vowels sr not
ch = input("enter the number:")
if ch in "aioueAIOUE":
    print("vowels")
else:
    print("Consonent")

# WAP to check the number is even or odd?
num = int(input("enter the number:"))
if num % 2 == 0:
    print(num, "even number")
else:
    print("odd number")
