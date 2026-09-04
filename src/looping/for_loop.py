#WAP to a number using for loop?
'''num = 456
for i in str(num):
    print(i)'''
'''# WAP to the sqaure of the number?
num = 456
for i in str(num):
    print(int(i*2))'''
# WAP to Print Palindrom number?
num = input("enetr the number:")
rev = " "
for i in num:
    rev = rev + i

if num == rev:
    print("palindrom number")
else:
    print("not palindrom")

