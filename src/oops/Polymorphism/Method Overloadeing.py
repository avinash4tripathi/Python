class demo:
    def calculate(self, *args):
        if len(args) == 1:
            print(args[0] ** 2)

        elif len(args) == 2:
            print(args[-1] - args[-2])

        elif len(args) == 3:
            print(args[1] + args[2])

        else:
            print(sum(args))


ob1 = demo()
ob1.calculate(10)
ob1.calculate(10, 20)
ob1.calculate(10, 20, 30)
ob1.calculate(10, 56, 45)
