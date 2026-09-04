class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"person name is {self.name} my age is {self.age}"


ob1 = person("jai", 26)
ob2 = person("Shivam", 24)
print(ob1)


class demo:
    def __init__(self, list1):
        self.list1 = list1

    def __str__(self):
        return f"{self.list1}"

    def __getitem__(self, index):
        return self.list1[index]

    def __setitem__(self, index, value):
        self.list1[index] = value
        # Continue with photo
