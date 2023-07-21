#creating a game for guessing until the user type the secret word
#-- from codeacedamy
import random

secret_word = ['tree','sun','ball','moon','earth','grass','world']
guess = ""
trial_count = 0
out_of_guesses = False
sword = random.choice(secret_word)
while guess != sword and not(out_of_guesses):
    if trial_count < 3:
        guess = input("Enter your guess word: ")
        trial_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print(f"You lose! The word is {sword}")
else:
    print(f"You got it! The word is {sword}")
