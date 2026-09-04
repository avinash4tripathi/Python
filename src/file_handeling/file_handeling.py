from pathlib import Path 
import os

def readfileandfolder():
   path = Path('')
   items = list(path.rglob('*'))
   for i,items in enumerate(items):
      print(f"{i+1} :  {items}")


def createfile():
  try:
      readfileandfolder()
      name = input("plese tell your file name: ")
      p = Path(name)
      if not p.exists():
       with open(p,'w') as fs:
         data = input("what you want to right:")
         fs.write(data)
       print(f"file created sucessfully")
      else:
        print("this file already exist")
  
  except Exception as err:
      print(f"an erroe as {err}")

def readfile():
  try:
       readfileandfolder()
       name = input("which file you want to read")
       p = Path(name)
       if p.exists() and p.is_file():
         with open(p,'F') as fs:
           data = fs.read()
           print(data)
         print("Readed Sucessfully") 
       else:
         print("the file doesnot exist")
  except Exception as err: 
    print(f" An error occured as {err}")

def updatefile():
  try:
       readfileandfolder()
       name = input("tell which file you want to update:")
       p = Path(name)
       if p.exists() and p.is_file():
          print("press 1 for changeing the name of your file")
          print("press 2 for overwriting the data of your file")
          print("press 3 for appending some content in your file ")

          res = int(input("tell your response:"))

          if res == 1:
             name2 = input("tell your file name:")
             p2 = Path(name2)
             p.rename(p2)

          if res == 2:
             with open(p,'w') as fs:
                data = input("tell what you want write this is overwriting the data") 
                fs.write(data)

          if res == 3:
             with open(p,'a') as fs:
               data = input("tell what you want to append")
               fs.write(""+data)
  except Exception as err:
      print("an error occured as {err}")

def deletefile():
   try:
       readfileandfolder()
       name = input("which file you want to delete:")
       p = Path(name)

       if p.exists() and p.is_file():
           os.remove(p)
           print("file removes sucessfully")
       else:
           print("Print no such file exist")
   except Exception as err:
       print(f"An error occured as {err}")


print("press 1 for creat file")
print("press 2 for read file")
print("press 3 for update file")
print("press 4 for delete file")

check = int(input("enter tell your massage :"))
if check == 1:
  createfile()
if check == 2:
  createfile()
if check == 3:
  updatefile()
if check == 4:
  deletefile()
