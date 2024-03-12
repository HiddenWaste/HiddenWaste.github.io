#Chord Game ill slowly add audio generative code into

#Spit out a random chord and give time to play the chord before next is given
#Save chord progression generated each session for display
#Later make it key Specific?
# each chord has an a and b section
# A is the root note
# B is Major, Minor, Diminished, or Augmented but start with just major and minor

import random, time

#Arrays for randomly Building a chord
rootNotes = ["A", "B", "C", "D", "E", "F", "G"] #Just all natural roots now, flats and sharps later
chordType = [" Major", " Minor"]

print("Welcome to the Chord Game!")

i = 0   #Iterable used in chord progression array
chordProgression = [] #chord Progression array

#Start of the game loop
print("Let the Chord Game Begin!!!")
while(1):
    #Create and Print generated chord / Add it to the progression array
    randomChord = random.choice(rootNotes) + random.choice(chordType)
    chordProgression.append(randomChord)
    print(randomChord)      #Will have to fix format of printing
    
    #Break after a 4 chord progression
    if(len(chordProgression) == 4):
        break

    #Time to find and play given chord
    time.sleep(6)

print('The Final Chord Progression: ', chordProgression)
print('Thanks for Playing!')