#Initializing Kokoro.....

#Heres the first kokoro specific program for this year
#Gonna be for minigames with simple code like hangman or rps 
#So that it is all in one file and not so many tiny files.

#okay so maybe Ill wait a bit before combining them all into one
#Until I have a better Idea for an overarching connection between them All

#Some Ideas:
    # Save high scores for each game that would have points/most num of tries
        #Would need to also save inputed names for the scores

#For now build a program to run each of them when chosen and to successfully stop
# one program and move to the next without needing to restart program entirely

#Importing files
import Hangman, CrackTheWord, SimpleChordGame


#Intoduction and game choosing
print("Welcome to Kokoro's Minigames!")
chosenGame = input("Hangman, Crack the Word, or Simple Chord Game? ->")

if chosenGame == "Hangman":
    Hangman
elif chosenGame == "Crack the Word":
    CrackTheWord
else:
    SimpleChordGame

print("Heres the end of my minigames program, come again soon!")