import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")
length = len(chosen_word)

display = []

for _ in range (0, length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range (0, length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)        