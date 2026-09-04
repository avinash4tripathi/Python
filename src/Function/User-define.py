# WAP to add two numbers by the help of fun.
def add():
    a = int(input("enter the number:"))
    b = int(input("enter your number:"))
    res = a + b
    print("result of addition is", res)


add()


# WAP to multiple two number?
def mul(a, b):
    res = a * b
    print("result of multiplication is: ", res)


mul(2, 4)
mul(25, 4)


# WAp to fact of a number?
def fact_number(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)


fact_number(int(input("enter your number:")))


def facbonaic():
    length = int(input("enter your number:"))
    n1 = 0
    n2 = 1
    print(n1, n2, end="")
    for i in range(length - 2):
        next = n1 + n2
        print(next, end=" ")
        n1 = n2
        n2 = next


facbonaic()
facbonaic()


# WAP to N natural number?
def natural_num(n):

    for i in range(1, n + 1):
        print(i)


natural_num(int(input("enter your number:")))


def add():
    a = int(input("enter your number:"))
    b = int(input("enter your number:"))
    c = a + b
    print(c)


add()
