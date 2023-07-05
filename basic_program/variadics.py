# modifying the averaging projects
# adding positional arguments instead of single python lists
# and add keyword argument 'round_to'

def calculate_average(*numbers, round_to=2):
    if not numbers: # numbers == [] or len(numbers) == 0
        print("No numbers provided")
        return None

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    round_average = round(average, round_to)
    print(f"Count: {count}, Average: {round_average}")
    return round_average

calculate_average(11,52,32,23.000032,21,2.32, round_to=3)