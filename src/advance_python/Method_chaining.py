# s = "@@@@hELLO1111@@@@@"
# print(s.strip('@').upper().replace('1','*'))


class person:
    def __init__(self):
        self.name = None
        self.address = None

    def set_name(self, name):
        self.name = name
        return self

    def set_address(self, address):
        self.address = address
        return self

    def show(self):
        print(f"name {self.name},address{self.address}")
        return self


ob1 = person()
ob1.set_name("Avinash").set_address("UK").show()
print(ob1.name)
print(ob1.address)
