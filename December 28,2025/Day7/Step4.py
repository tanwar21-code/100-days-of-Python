import random
word_list = ["ardvark", "baboon", "camel"]

stages = [
    '''
  +---+
    |   |
        |
        |   |
        |   |
        ===''' 
        ,'''
  +---+
    |   |
    O   |
        |   |
        |   |
        ===''',
          '''
    +---+
    |   |
    O   |
    |   |
        |   |
        ===''', 
        ''' 
    +---+
    |   |
    O   |
   /|   |   
        |   |
        ===''',
          '''
    +---+
    |   |
    O   |   
   /|\  |   
        |   |
          ===''', 
          '''
    +---+
    |   |
    O   |  
   /|\  |
   /    |   |
          ===''',
            '''
     +---+
     |   |  
     O   |
    /|\  |
    / \  |   |
          ===''']

#TODO 1: create a variable to track the number of lives the user has. Set it to 6.
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

placeholder = '_'*len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
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
    

    

    


#TODO 2: if guess is not in the chosen_word, then reduce the number of lives by 1. If lives goes down to 0 then the game is over and the user loses.
    if guess not in chosen_word:
        lives -= 1
    
    if '_' not in display:
        game_over =True
        print('You WIn')
    elif lives == 0:
        game_over = True
        print('You lose')
    print(f'You have {lives} lives left')

#TODO 3: print the ASCII art from 'stages' that corresponds to the number of lives the user has remaining.lives = 6
    if lives == 6:
        print(stages[0])
    elif lives == 5:
        print(stages[1])    
    elif lives == 4:
        print(stages[2])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[4])
    elif lives == 1:
        print(stages[5])
    elif lives == 0:
        print(stages[6])