#writing conditions using if statement

user_name = input("What is your name? ")
print("Hello " + user_name + "!")
user_age = input("How old are you " + user_name + "? ")
is_single = input("Are you single? [Yes or No]")
if int(user_age) <= 17: #you can use 'and' 'or' 'not' operator for many conditions in one if statement
    if is_single == "Yes":
        print("Good! Focus on study, okay?")
    elif is_single == "No":
        print("Hayst!")
    else:
        print("Please clarify your answer.")
elif int(user_age) > 17:
    if is_single == "Yes":
        print("Nice. Wanna hang out?")
    elif is_single == "No":
        print("Bah!")
    else:
        print("Please clarify your answer.")