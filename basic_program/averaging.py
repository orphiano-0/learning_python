# create a calculate average using lists
# using a parameter
def calculate_average(numbers):
    sum = 0
    # checking if the lists is empty
    if len(numbers) == 0:
        print("No numbers provided")
    else:
        for number in numbers:
            # loop for adding all values in the lists
            sum = int(number) + sum
        # dividing them by their len
        average = sum / len(numbers)
        # printing
        print("Count: " + str(len(numbers)) + " Average: " + str(average))
# calling function
calculate_average([16,22,33,421,55,63])