word_list = ["ardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = '_'*len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []
#TODO 1: use a while loop to let the user guess again 
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    
    

    #TODO 2: change the for loop so that you keep the previous correct guesses in the display# and only add new correct guesses to the display
    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if '_' not in display:
        game_over =True
        print('You WIn')