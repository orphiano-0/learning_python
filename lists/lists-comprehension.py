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