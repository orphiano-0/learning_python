# checking the most repeated number in the list
numbers = [1, 2, 3, 5, 6, 7, 5, 4, 4, 2, 1, 1, 1, 2, 5, 7]
mode = max(numbers, key=numbers.count)
print(mode)