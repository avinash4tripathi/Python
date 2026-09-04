n = int(input("enter the number: "))
try:
     print(10/n)
except Exception as err:
     print("soory you can not divide by 0")

else:
     print("good there is no exception")

finally:
     print("no matter what but i will run at even time")

print("ok I have  done the division")