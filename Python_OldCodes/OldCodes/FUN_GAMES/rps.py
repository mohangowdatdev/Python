
import random
import time
from gtts import gTTS
from pygame import mixer
import os

print("___________________________________________________________________________________________________")

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text = audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # check if the file is playing
            pass
        mixer.music.load("ac.mp3")
        os.remove("audio.mp3")

def speak(audio):
    for line in audio.splitlines():
        text_to_speech = gTTS(text = audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # check if the file is playing
            pass
        mixer.music.load("ac.mp3")
        os.remove("audio.mp3")

name = input("What is you name: ")
talk("|| Welcome to the game "+ name + " ||")
talk("Here are quick tips on how to play the game:- ")
print("___________________________________________________________________________________________________")

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock v/s Paper-> Paper wins \n"
      + "Rock v/s Scissor-> Rock wins \n"
      + "Paper v/s Scissor-> Scissor wins \n")
time.sleep(2)
print("___________________________________________________________________________________________________")

talk("We will begin the game in")

for i in [5, 4, 3, 2, 1]:
    talk(str(i))

cw=0
uw=0
tt=0
print("___________________________________________________________________________________________________")
print("---------------------------------------------------------------------------------------------------")
while True:
    print("___________________________________________________________________________________________________")
    print("Enter your choice: \n 1. Rock \n 2. paper \n 3. scissor")
    speak("Enter you choice "+ name)
    print("----------------------")
    print()
    choice = int(input(name +" turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        choice_name = 'ROCK'
    elif choice == 2:
        choice_name = 'PAPER'
    else:
        choice_name = 'SCISSOR'

    print(name + " : " + choice_name)
    speak("your choice is " + choice_name)

    print()
    print("----------------------")
    print()
    talk("Now its computer turn.......")
    talk("ROCK.  PAPER.  SCISSOR")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSOR'

    print("Computer: " + comp_choice_name)
    speak("Computer choice is "+comp_choice_name)

    print()
    print("----------------------")
    print()
    print("___________________________________________________________________________________________________")

    talk("|| Head to Head ||")
    print()
    print(choice_name + " V/s " + comp_choice_name)
    print("----------------------")

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("PAPER WINS => ", end="")
        result = "PAPER"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("ROCK WINS =>", end="")
        result = "ROCK"
    else:
        print("SCISSOR WINS =>", end="")
        result = "SCISSOR"

    if result == choice_name:
        talk("  | Hooray "+name+" wins | ")
        uw=uw+1
    else:
        talk("  | Computer wins. Try Again |")
        cw=cw+1
    tt=tt+1

    print()
    print("Do you want to play again? (Y/N)")
    speak("Do you want to continue playing. If yes then click y or else click n")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print()
print()
print("______________________________________________________________________________________________________")
talk("Please wait a second for your results to declare.")
time.sleep(2)
print("Total number of wins by " + name+ ": ", uw)
print("Total number of wins by Computer: ", cw)
print("Total games played: ", tt)
per= uw/tt*100
print("Your win percentage for current game is " + str(per) + "%")
if per>=80 and per<=100:
    speak("Congragulations "+name +". You have a Good win percentage of " + str(per) +" percentage")
elif per>=50 and per<80:
    speak("Congragulations "+name +". your win percentage is " + str(per) + ".  Yet you can improve a lot.")
elif per>=20 and per<50:
    speak("You can improve your skills. your win percentage is " + str(per))
else:
    speak("You have to increase your skills. your win percentage is " + str(per))
print("______________________________________________________________________________________________________")