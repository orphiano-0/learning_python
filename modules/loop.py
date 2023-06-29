#--WHILE LOOP
#creating variables and conditions
import time

number = 1
while number <= 5: #condition
    print(number)
    time.sleep(2.3) #not necessary, just for some cool countdown.
    number += 1
print("Done")

#--FOR LOOP
#looping in every letter in a string
for letter in "Nice home!":
    print(letter)
#looping in array
characters = ["Grey", "Cecil", "Nico"]
for character in characters:
    print(character)
#looping in numbers
for number in range(10): #always minus 1
    print(number)
