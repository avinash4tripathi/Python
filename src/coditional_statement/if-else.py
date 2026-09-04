# Q. WAP check the number is start with one or not
num = input("enter the number: ")
if str(num)[0] == "1":
    print("start with 1")
else:
    print("not start witn one")

# Q. WAP TO CHECK THE NUM IS STARTING AN ODD VALUE OR EVEN VALUE
num = int(input("enter the number: "))
num1 = int(str(num)[0])
if num1 % 2 == 0:
    print("even")
else:
    print("odd")

# Q.WAP TO CHECK THE NUMBER IS PALIDROM NUMBER OR NOT
num = int(
    input("enter the number")
)  # It bascially repeating the value in the first and second.
num1 = str(num)
if num1[::-1] == num1:
    print("plaidorm")
else:
    print("not palindrom")
