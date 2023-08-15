#2d lists and nested loops

#2d lists have rows and columns which needed to be called at.
nicknames = [
    ["Gab", "Mike", "Lid"],
    ["Lyn", "Dan", "Lits"],
    ["Bolt", "Spot", "Dicks"],
    ["Kang"]
]
print(nicknames[2][1])

#nested for loop
for row in nicknames:
    for column in row:
        print(column)