def doing_something(myself):
    def wrapper():
        print("I am doing something!")
        return myself()
    return wrapper

@doing_something # @ pie decorator syntax
def cook():
    print("I am cooking!")
    return
@doing_something
def wash():
    print("I am cooking!")
    return
def clean():
    print("I am cooking!")
    return

doing_cleaning = doing_something(clean)
cook()