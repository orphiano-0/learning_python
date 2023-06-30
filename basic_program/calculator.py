print("Welcome to my self-made calculator")
try:
    first_num = float(input("Please enter your first number: "))
    second_num = float(input("Please enter your second number: "))
    operator = input("Please select an operator: [+, -, *, /] ")

    if operator == "+":
        print(first_num + second_num)
    if operator == "-":
        print(first_num - second_num)
    if operator == "*":
        print(first_num * second_num)
    if operator == "/":
        print(first_num / second_num)
    else:
        print("Invalid operator")
except ValueError as error:
    print(error)