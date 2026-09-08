# Int: These are numbers represented on the number line: positive, negative, and zero.
a = 25
print(type(a))

# Float: A number that contains decimal values is known as a float.
a = 10.2
print(type(a))

# Complex: A combination of real and imaginary numbers in the form a + bj or a - bj.
# Here, a is the real part and bj is the imaginary part.
a = 4 + 5j
print(type(a))

# Boolean: A data type with two possible values, True and False.
a = 9.8
bool(a)

# Multivalued data types are collections of individual values:
# string, list, tuple, set, and dictionary.

# String: A collection of characters, numbers, and special characters inside quotes.
a = "avinash tripathi"
print(type(a))

# Indexing gives access to an individual character in a sequence.
# Slicing extracts a portion of a sequence using indexes.

# Find the character at index 3 in the string "python".
a = "python"
print(a[3])

# Find the reverse of a string.
a = "python"
print(a[::-1])

# List: A collection of homogeneous or heterogeneous data stored inside square brackets.
# Lists are mutable, so values can be added, updated, or removed.
a = [1, 2, 3, 4, 5]
a.append("hello")  # Add a value at the end.
print(a)

a = [1, 2, 3, 4.5]
a.insert(3, 25)  # Add a value at the specified index position.
print(a)

a = [1, 2, 3, 4, 5, 6]
a.pop(5)
print(a)

# Tuple: A collection of homogeneous or heterogeneous data stored inside parentheses.
# Tuples are immutable, so their values can be accessed but not modified.
a = ("apple", "Mango", "Graps")
print(a)
print(a[0])
print(a[1])

a = ("apple", "Mango", "Graps")
# a[0] = "Orange"
print(a)

# Set: An unordered collection stored inside braces.
# Because sets are unordered, indexing is not supported.
# Sets are mutable, but their elements must be immutable values.
a = {
    1,
    2,
    3,
    4,
    8,
    9,
    46,
}
print(a)

# Convert a float data type into an integer.
a = 2.5
print(type(int(a)))
