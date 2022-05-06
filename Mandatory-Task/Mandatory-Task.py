import pyttsx3
import pyjokes
from datetime import datetime
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def speak(a):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume', 5.0)
    engine.say(a)
    engine.runAndWait()

def wish_user():
    hour=datetime.now().hour
    if hour>=5 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=17:
        speak("good afternoon")
    else:
        speak("good evening")

def jokes():
    joke=pyjokes.get_joke(language="en", category="all")
    speak(joke)
    speak("haha")

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")

def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(current_time)


if __name__=="__main__":
    wish_user()
    speak("Let me start our converstation with a random joke")
    jokes()
    speak("Would you like to know the weather conditions for your city?")
    response=input("Y/N ->")
    if response=="Y" or response=="y":
        speak("Enter your City's name")
        city = input("Enter the Name of City ->  ")
        city = city+" weather"
        weather(city)
        speak("I have printed them on your screen")
    elif response=="N" or response=="n":
        speak("I see, okay then. Sad.")
    else:
        speak("invalid character sobs")
    speak('Right now i can do the following things for you:')
    speak("Tell you another joke or tell you the current time. What would you like me to do?")
    print("1. Another joke")
    print("2. Time")
    opt_num=int(input("Enter your option number:"))
    if opt_num==1:
        jokes()
    elif opt_num==2:
        current_time()
    else:
        speak("Invalid Number")

    speak("With this my master would like me to stop running, what a sad soul I am. If you would like to talk to me again, rerun the code. I will be waiting for you, love")


