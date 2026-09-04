def square(x):
    return x * x


def calculate(func, value):
    return func(value)


result = calculate(square, 5)
print(result)
