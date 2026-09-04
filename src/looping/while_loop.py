# print narural number from n1 to n2.
"""n1=int(input("enter the number"))
n2=int(input("enter the number"))
while n1<= n2:
     print(n1)
     n1 += 1"""

# WAP even number natural number
"""n=int(input("enter the number: "))
i=2
while i <= n :
      i%2 == 0
      print(i)
      i += 2
    OR"""

# second method.
"""n = int(input("enter the number :"))
i=1
while i<=n:
    if i%2 == 0:
        print(i)
        i+=1"""
# for odd number?

"""n=int(input("enter the number: "))
i=1
while i <= n :
      i%2 != 0
      print(i)
      i += 2"""
# WAP to sum of n natural number

n = int(input("enter the number:"))
i = 1
add = 0
while i <= n:
    add += i
    i += 1
print(add)
