import timeit
tuple = ("Gab", 20, "Single")
print(tuple)
#iterate tuple using for loop
def iterate():
    for item in tuple:
        print(item)

#checking elements if the element is in tuple using if statements
def check():
    if "Gabr" in tuple:
        print("Nice!")
    else:
        print("Not nice!")
#time it in, which one is faster.
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]", number = 1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)", number = 1000000))
#much more efficient on working with tuples
