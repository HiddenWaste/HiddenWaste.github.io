#Chord Game additions/testing
import random, time

#Arrays for randomly Building a chord
#Root note array contains all flats, sharps, and naturals
#Chord Type now includes major seven and minor seven chords
rootNotes = ["A", "B", "C", "D", "E", "F", "G", "Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "A#", "B#", "C#", "D#", "E#", "F#", "G#"] 
chordType = ["M", "m", 'M7', 'm7']

#Overead while loop to replay chord game if wanted
while(1):
    #Start of the game loop
    print("Let the Chord Game Begin!!!")

    #reset / declare chord Progression array
    chordProgression = [] 

    #Loop for making chords and the chord progression
    while(1):
        #Create chord, add it to progression, then print created chord
        randomChord = random.choice(rootNotes)+random.choice(chordType)
        chordProgression.append(randomChord)
        print(randomChord)   

        #Time to find and play given chord
        time.sleep(3)

        #After 4 chords show progression and ask to play again
        if(len(chordProgression) == 4):
            #Chord progression printing
            print('The Final Chord Progression: ', chordProgression)
            break

    #Play again?
    playAgain = input("Would you like to play again? y/n   ")

    #If statement to repeat or break
    if (playAgain == 'y'):
        print("Run it back!")
    elif (playAgain == 'n'):
         print('Hope you come again!')
         break