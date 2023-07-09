def hello(name):
    print(f"Hello, {name}!")
def comp_name_greeting(fname, lname):
    print(f"Hello, {fname} {lname}!")
comp_name_greeting("Gabriel", "Orphiano")

def greet(*names):
    # * accepts unlimited arguments
    print(f"Hello {' and '.join(names)}")
    # it will print... Hello name and name and name and name...
greet("Gabriel", "Arthur", "Tessia", "Bern", "Jin")

def data(**information):
    # creating some sort of dictionary but no limited
    for key, value in information.items():
        print(f"{key}: {value}")
data(name="Gabriel", age=20, address="Valenzuela", gender="Male")

# you can have both arguments as parameters at the same function
def func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
func("Gabriel", "Orphiano", "orphiano-0", gmail="gab.orphiano@gmail.com", gender="Male")
print(func)