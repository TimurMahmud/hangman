import random

word_list = ["apple", "banana", "grape", "pear", "tomato"]

print(word_list)
1
word = random.choice(word_list)

print(word)

print("Enter a single letter:")
guess = input()
if len(guess) != 1 or guess.isalpha() != True:
    print("Oops! That is not a valid input.")
else:
    print("Good guess!")
