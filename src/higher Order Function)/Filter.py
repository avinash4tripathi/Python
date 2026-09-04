# filter()
numbers = [1, 2, 3, 4, 5, 6]


def even(x):
    return x % 2 == 0


result = filter(even, numbers)
print(list(result))

# The even() function checks whether each number is even.

# The even function is passed to filter(), making filter() a Higher-Order Function.
