import time
import random
from gtts import gTTS
from pygame import mixer
import os



list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text = audio, lang='en-uk')
        text_to_speech.create('audio.mp3')
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
        text_to_speech.create('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # check if the file is playing
            pass
        mixer.music.load("ac.mp3")
        os.remove("audio.mp3")

talk("||Welcome to the game||")
talk("The game is simple")
talk("I will guess a number, and you will have to predict it in 10 moves and 90 seconds. I will be providing you hint in every prediction you make wrong.")
talk("Let's begin the game. Now close your eyes until I say you to open")
time.sleep(5)

rn = random.choice(list)
print("The Random number I picked was : [", rn,"]")

for i in range(30):
    time.sleep(0.05)
    print(".")

talk("Open your eyes and try to predict a number. Good luck. Your time begins now")
start=time.time()

i=0
while True:
    i=i+1
    gn = int(input("Enter your predicted number: "))
    if (rn - gn) <= 5 and (rn - gn) >= 1:
        talk("ALMOST CORRECT")
    elif (rn - gn) <= 10 and (rn - gn) >= 6:
        talk("BIT NEAR")
    elif (rn - gn) >= -5 and (rn - gn) <= -1:
        talk("ALMOST CORRECT")
    elif (rn - gn) >= -10 and (rn - gn) <= -6:
        talk("BIT NEAR")
    elif rn == gn:
        talk("|You are perfect. You can scroll to the top and check the number|")
        break
    else:
        talk("||TOO FAR||")
    if i>10:
        talk("Sorry You are out of moves, TRY AGAIN")
        talk("Your number was ")
        talk(gn)
        break

    if gn > 50 or gn < 0:
        talk("Please Enter a number only between 0 and 50")
print()
print()
end= time.time()
tt=int(end-start)
if tt > 90:
    talk("We are sorry, You ran out of time. You only had 90 seconds.")
if i<=10 and tt<=90:
    talk("Congratulations, You have identified the correct element "+ str(gn) +" in")
    talk(str(i) + " counts")
    speak("and")
    talk(str(tt)+" seconds")



