dictionary = {
    "Name": "Gabriel",
    "Age": 20,
    "Address": "Valenzuela"
}
dictionary_2 = {
    "Name": "Gabriel",
    "Age": 19,
    "Address": "Valenzuela"
}
print(dictionary)

def add_value():
    dictionary["Status"] = "Single"
    print(dictionary)
def del_value():
    del dictionary["Status"]
    print(dictionary)

def update_value():
    dictionary.update(dictionary_2)
    print(dictionary)
