print("Guess an animal which a long neck and is herbivorous")
secretword = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess.lower() != secretword and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Whats your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses , You Lose!!!")
else:
    print("You win!!")
