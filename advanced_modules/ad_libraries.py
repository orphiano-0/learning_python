import random
import cowsay
from prettytable import PrettyTable # You can download package from outside source using pip
# You can call specific function in a library using syntax 'from' and 'import'
table = PrettyTable(["Names", "Age", "Address", "Status"])
table.add_row(["Art", 19, "Ashber", "Single"])
table.add_row(["Tess", 20, "Elshire", "Single"])
print(table)

# random library
# -- random
coin = random.choice(["heads", "tails"])
print(coin)
# -- shuffle
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# cowsay lib
cowsay.cow("Hello, Gab!")