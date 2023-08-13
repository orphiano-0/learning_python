import calendar
import time

print("Let's check if the year is a leap year or not!")
year_input = int(input("Enter a specific year: "))

checker = calendar.isleap(year_input)

if checker == True:
    print("Checking...")
    time.sleep(2)
    print("The year is a leap year")
else:
    print("Checking...")
    time.sleep(2)
    print("The year is not a leap year")