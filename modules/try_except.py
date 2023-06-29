#-- applying try except block can avoid error from invalid input etc
try:
    #value = 12/0
    age = int(input("What is your current age? "))
    print(age)
except ValueError: #specific exception
    print("Invalid input!")
except ZeroDivisionError as err:
    print(err)