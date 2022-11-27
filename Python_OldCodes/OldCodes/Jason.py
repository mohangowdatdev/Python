from gtts import gTTS
import speech_recognition as sr
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import requests
from pygame import mixer
import urllib.request
import urllib.parse
import bs4

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text = audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()

def mycommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("JASON is hearing you!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        print("analysing....")

    try:
        command= r.recognize_google(audio).lower()
        print("you said: " + command + "\n")
        time.sleep(1)


    except sr.UnknownValueError:
        print("Your command couldn't be heard" )
        command = mycommand();

    return command

def tars(command):
    errors=["I don't know what do you mean", "Excuse me?", "Can you repeat it please!!", "I didn't quite get that"]
    "if command for executing statements"

    #search on google
    if "open google and search" in command:
        reg_ex = re.search("open google and search (.*)",command)
        search_for = command.split("search",1)[1]
        print(search_for)
        url= "http://www.google.com/"
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + "r/" + subgoogle
        talk("okay!")
        driver = webdriver.Firefox(executable_path= "/home/coderasha/Desktop/geckodriver")
        driver.get("http://www.google.com")
        search = driver.find_element_by_name("q")
        search.send_keys(str(search_for))
        search.send_keys(Keys.RETURN)

    elif 'email' in command:
        talk("What is the subject?")
        time.sleep(3)
        subject = mycommand()
        talk("What should I say?")
        message = mycommand()
        content = "Subject: {}\n\n{}".format(subject, message)

        #init gmail SMTP
        mail = smtplib.SMTP("smtp.gmail.com",587)
        #identify to server
        mail.ehlo()
        #encrypt session
        mail.starttls()
        #login
        mail.login("your_mail","your_mail_password")
        #send message
        mail.sendmail("FROM","TO",content)
        #end mail connection
        mail.close()

        talk("Email sent")

    #search in wiki
    elif "wikipedia" in command:
        reg_ex = re.search("wikipedia (.+)",command)
        if reg_ex:
            query = command.split("wikipedia",1)[1]
            response = requests.get("https://en.wikipedia.org/wiki/" + query)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, "html.parser")
                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                for para in paragraphs:
                    print(para.text)
                intro='\n'.joint([para.text for para in paragraphs[0:3]])
                print(intro)
                mp3name = "speech.mp3"
                language = "en"
                myobj = gTTS(text=intro, lang=language, slow=False)
                myobj.save(mp3name)
                mixer.init()
                mixer.music.load("speech.mp3")
            while mixer.music.play():
                if "stop" in command:
                    mixer.music.stop()

    #search vds in youtube
    elif "youtube" in command:
        talk("Ok!")
        reg_ex = re.search("youtube(.+)", command)
        if reg_ex:
            domain = command.split("youtube",1)[1]
            query_string = urllib.parse.urlencode({"search_query": domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"href=\"\/watch\?v=(.{11})", html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass

    elif "hello" in command:
        talk("Hello, I am TARS. How can I help you?")
        time.sleep(1)
    elif "who are you" in command:
        talk("I am one of the four former US Marine Corps tactical robot")
        time.sleep(1)
    else:
        error=random.choice(errors)
        talk(error)
        time.sleep(1)

talk("JASON is hearing you!")

while True:
        time.sleep(2)
        tars(mycommand())












