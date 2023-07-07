from operator import add
add(1,2)
def double(func):
    def inner(*args):
        print(func(*args) * 2)
    return inner
double_add = double(add)
double_add(1, 2)
double_add(6,23)