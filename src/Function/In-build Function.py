s="This is your homework which should be done tomorrow"
res = []
list1 = s.split()
for word in list1:
    if len(word)>= 5:
        res.append(word)
print(res)



s= "This is your homework which should be done tomorrow Avianshtripathi"
largest = ''
list1 = s.split()
for word in list1:
    if len(word)>=len(largest):
     largest = word
print(largest)
