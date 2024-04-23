import random
from tkinter import END

#Introduction
print('Welcome to Hangman!')

#Creating word bank and other variables
wordBank = ['plane', 'bible', 'monologue', 'cat', 'bark', 'kahuna', 'chihuahua', 'bubble']
tries = 10
correct = 0

#function for checking a guess
def checkGuess(letter):   
    global i            #Global variables so the function works
    i = 0

    #Search word for letter and reveal if present
    for len in secretWord:
        if secretWord[i] == letter:
            print(f'There is a {letter} at position {i} in the word.')
            displayWord[i] = letter
        #Increment i    
        i = (i + 1)
    #Reset i
    i = 0

#Game Start
while(int(tries) != 0):
    #have com choose word   
    secretWord = wordBank[random.randint(0,7)]

    #Create the shown form of the word
    displayWord = []
    for len in secretWord:
        displayWord.append('*')
    
    #collect user guess and play game
    while(int(tries) != 0):
        #print shown word
        print(f'{displayWord}')

        #Collect New Guess
        guess = input('---->')
        
        #Check New Guess
        checkGuess(guess)

        #Make Sure Game not finished
        if secretWord.find("*") == -1:
            print('You won!')
            break

        #increment tries
        tries = (tries - 1)
        print(f'tries left: {tries}')

if tries == 0:
    print("Sorry you lose")
    print("The secret word was", secretWord)