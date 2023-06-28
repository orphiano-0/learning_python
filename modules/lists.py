#storing different values in a list
characters = ["Arthur", "Regis", "Sylvie", 232, False, True, 23, "Eralith"]
print(characters[2]) #accessing specific value in a list, according to its index
print(characters[3:]) #accessing values from index 3 to end without printing the index 0 to 2

characters[5] = 88 #changing specific value in a list
print(characters[5])

#examples of lists function
lists_numbers = [51, 225, 31, 4, 53, 66, 27]
characters.extend(lists_numbers) #extend function.
lists_numbers.append(8) #append new value in the lists
lists_numbers.insert(4, 5.5) #inserting value in specific index
lists_numbers.remove(27) #removing specific value existing in lists
lists_numbers.pop() #getting rid of the last value in the lists
lists_numbers.sort() #sorting values in ascending manner

same_numbers = lists_numbers.copy() #declaring new lists and copying the values
lists_numbers.clear() #clear all values in the lists
print(lists_numbers)
print(same_numbers)