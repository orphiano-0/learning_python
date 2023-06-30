#reading file
def reading_file():
    database = open("../files/database.txt", "r")
    for data in database.readlines():
        print(data)
    print(database.readlines()[2])
    database.close()

#appending files
def appending_file():
    database = open("../files/database.txt", "a")
    database.write("\nNike - Shoes")
    database.close()
def writing_file():
    database = open("../files/database_two.txt", "a")
    database.write("\nNike - Shoes")
    database.close()
