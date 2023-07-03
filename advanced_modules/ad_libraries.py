import json
import random
import cowsay
import requests
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
cowsay.trex("Hello, Gab!")

# requests lib
# -- database that has json values
link = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=eminem")
# print(json.dumps(link.json(), indent=2))
object = link.json()
# the key 'results' has a value named trackName
# printing 20(check the limits in url) values of trackName in that list
for results in object["results"]:
    print(results["trackName"])