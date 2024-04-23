import random

#RPS!
userScore = 0
comScore = 0

print('Welcome to RPS! First to 10 wins.')

#Overall game loop
while(1):
    choices = ['rock', 'paper', 'scissors']
    comChoice = random.choice(choices)
    userChoice = input('Your choice -->')

    #lead in to choice reveal / choice reveal
    print('Rock')
    print('Paper')
    print('Scissors')
    print('Shoot!')
    print('You -> ',userChoice)
    print('Com -> ',comChoice)

    if userChoice == 'rock' and comChoice == 'scissors':   #User win Scenarios
        print('Rock breaks scissors, you win!')
        userScore = userScore + 1
    elif userChoice == 'paper' and comChoice == 'rock':
        print('Paper covers rock. You win!')
        userScore = userScore + 1
    elif userChoice == 'scissors' and comChoice == 'paper':
        print('Scissors cut paper. You win!')
        userScore = userScore + 1
    elif userChoice == comChoice:                         #in case of a tie
        print('Its a tie!')
    elif userChoice == 'rock' and comChoice == 'paper':     #User lose scenarios
        print('Sorry, paper cover rock, you lose')
        comScore = comScore + 1
    elif userChoice == 'paper' and comChoice == 'scissors':
        print('Sorry, scissors cut paper. You lose.')
        comScore = comScore + 1
    elif userChoice == 'scissors' and comChoice == 'rock':
        print('Sorry, rock breaks scisors. You lose.')
        comScore = comScore + 1

    #Print out the scores
    print('userScore: ',userScore)
    print('comScore: ',comScore)

    #Game ending conditions
    if (userScore == 10):
        print('You win RPS!')
        break
    elif (comScore == 10):
        print('Sorry, game over.')
        break
