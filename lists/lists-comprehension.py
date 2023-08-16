# lists comprehension

orig_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lists = []
for i in orig_lists:
    times = i * 2
    new_lists.append(times)
print(new_lists)

# good practice
# new_lists = [new_item for item in lists]
orig_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lists = [i * 2 for i in orig_lists]
print(new_lists)

language = 'Python'
new_language = [i for i in language]
print(new_language)

# conditional lists comprehension
orig_numbers = [1, 2, 3, 4, 5, -1, -32, -31, -52, 100, -21]
# a condition is set up
new_numbers = [i * 2 for i in orig_numbers if i % 2 == 1]
print(new_numbers)

# if else condition in list comprehension
new_number_lists = [i if i > 0 else 0 for i in orig_numbers]
print(new_number_lists)

# challenge -- squared the negative item in the lists
squared_numbers = [i**2 for i in orig_numbers if i < 0]
print(squared_numbers)

# checking if the letter is consonant and vowels in list
sentence = 'Python language'
def is_consonant(i):
    vowels = 'aeiou'
    return i.isalpha() and i.lower() not in vowels
def is_vowels(i):
    vowels = 'aeiou'
    return i.isalpha() and i.lower() in vowels
# checkers
consonant_checker = [i for i in sentence if is_consonant(i)]
print(consonant_checker)

vowel_checker = [i for i in sentence if is_vowels(i)]
print(vowel_checker)