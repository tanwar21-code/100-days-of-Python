word_list = ["ardvark", "baboon", "camel"]
import random

chosen_word = random.choice(word_list)
print(chosen_word)

#TODO 1: Create a 'Placeholder' with the same number of underscores as the letters in the chosen_word. For example, if the chosen_word is "apple", the placeholder should be "_ _ _ _ _". Print the placeholder.
placeholder = '_'*len(chosen_word)
print(placeholder)

#TODO 2: create a 'Display' that puts the guessed letter in the correct position(s) of the placeholder if the guessed letter is in the chosen_word. If the guessed letter is not in the chosen_word, the placeholder remains unchanged. Print the updated placeholder after checking the guessed letter.
guess = input("Guess a letter: ").lower()
print(guess)

# placeholder_list = list(placeholder)
# print(placeholder_list)

display = ''
# for i in range(0, len(chosen_word)):
#     if chosen_word[i] == guess:
#         placeholder_list[i] = chosen_word[i]
#     else:
#         continue
# for i in placeholder_list:
#         display += i
# print(display)

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += '_'

print(display)