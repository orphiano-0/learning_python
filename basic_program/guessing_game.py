#creating a game for guessing until the user type the secret word
#-- from codeacedamy

secret_word = "Humans"
guess = ""
trial_count = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if trial_count < 3:
        guess = input("Enter your guess word: ")
        trial_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Bah! You suck!")
else:
    print("Congrats!")
