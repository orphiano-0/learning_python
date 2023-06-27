#using a function to declare specific tasks
def addition():
    print(32 + 23)
def subtraction():
    print(32 - 23)
def multiplication():
    print(32 * 23)
def division():
    print(32 / 23)
def modulo():
    print(32 % 23)
def operations():
    addition()
    subtraction()
    multiplication()
    division()
    modulo()

operations() #calling a function to perform the functions stored in that function

#using parameter in a function
def calling_name(name):
    print("Hello, " + name + "!")
    #using a parameter to pass value in the function
    #it is possible to various information in a parameter
calling_name("Gabriel")
calling_name("Kathlyn")
