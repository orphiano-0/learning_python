print("Welcome to my self-made calculator")
first_num = float(input("Please enter your first number: "))
second_num = float(input("Please enter your second number: "))
operator = input("Please select an operator: [+, -, *, /] ")

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print("Invalid operator")
