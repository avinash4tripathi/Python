class school:
    sub1 = "math"


class Bachelor(school):
    sub2 = "chemistry"


class master(Bachelor):
    sub3 = "computer Science"


ob1 = master()
print(ob1.sub1)
print(ob1.sub2)
print(ob1.sub3)
