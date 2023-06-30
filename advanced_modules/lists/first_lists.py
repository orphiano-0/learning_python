mylist = ["Gabriel", "Orphiano", 20, "IT Student", "Single"]
number_list = [1, 2, 3, 4, 5, 6]
print(mylist)
print(len(mylist)) #checking how many items in the list
list = mylist[::2] #skipping every two index
print(list)

#specify via variable
def var_list():
    item = mylist[2: 5]
    print(item)
#iterate the list using for loop
def iterate_list():
    for items in mylist:
        print(items)
#checking if the item is in list
def check_list():
    if "Handsome" in mylist:
        print("Yes")
    else:
        print("No")
def square_list(): #squaring the value of item in list
    num_lists = [item * item for item in number_list]
    print(num_lists)


