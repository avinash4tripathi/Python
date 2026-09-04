class Bank:
    def __init__(self, bal):
        self.__bal = bal

    def check_bal(self):
        password = int(input("enter your password: "))
        if password == 2026:
            print(self.__bal)
        else:
            print("Unauthorized accees")


c1 = Bank(20000)
c1.check_bal()
