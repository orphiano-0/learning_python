database = open("../files/database.txt", "r")
for data in database.readlines():
    print(data)
#print(database.readlines()[2])
database.close()

