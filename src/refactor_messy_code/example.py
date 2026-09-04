"""def cal(a,b):
    x = a + b
    y = a * b
    print("Sum",x)
    print("product",y)

cal(10,20)"""

# then i refarctor the code.


def calculate_values(first_number: int, Second_number: int) -> None:
    """Calculate and display the sum and product of two numbers."""
    total = first_number + Second_number
    product = first_number * Second_number

    print(f"Sum: {total}")
    print(f"Product: {product}")


calculate_values(10, 20)
