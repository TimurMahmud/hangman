while True:
    guess = input("Guess a letter !")
    if len(guess) != 1 or guess.isalpha() != True:
        print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        print("you guessed: " + guess)
    break
