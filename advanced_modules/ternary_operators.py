# ternary operator are operator that evaluates something based on condition being True of False
# you can say it is a one line if-else statement

## Example:
# Without ternary operator
number = int(input("Enter a number: "))
# using if else statement
if number % 2 == 0:
    result = "even"
else:
    result = "odd"
# output
print(f"The number is {result}")

# With ternary operator
number = int(input("Enter a number: "))
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}")