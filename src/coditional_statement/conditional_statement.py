# WAP to check the Character is in Uppercase?
Char = input("enter the character: ")
if "A" <= Char <= "Z":
    print("Uppercase")
else:
    print("lowecase")

# Age Check (If-else)
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Nested-if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
