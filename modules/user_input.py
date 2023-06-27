#asking a user for inputs to add interactive experience
user_name = input("What is your name: ")
print("Hello, " + user_name + "!")

user_age = input("How old are you " + user_name + "? ")
print("Must be nice being " + user_age + " years old, huh?")

#basic addition using user's input
print("Let's play some addition game...")
number_one = input("Enter a first number: ")
number_two = input("Enter a second number: ")
result = int(number_one) + int(number_two)
print(result)