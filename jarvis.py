import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyautogui
import requests
from bs4 import BeautifulSoup
import pyjokes
import sys  # For sys.exit()
import os   # Import os module for os.system()

def initialize_voice():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use a female voice; change index if needed
    return engine

def speak(engine, audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(engine):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(engine, "Good Morning!")
    elif 12 <= hour < 18:
        speak(engine, "Good Afternoon!")
    else:
        speak(engine, "Good Evening!")
    speak(engine, "My name is Tenz sir, tell me how may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=60, phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you say that again?")
        return "None"

    return query.lower()

def TaskExecution():
    engine = initialize_voice()
    wishMe(engine)

    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak(engine, 'Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak(engine, "According to Wikipedia")
            print(results)
            speak(engine, results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(engine, f"Sir, the time is {strTime}")

        elif 'open' in query:
            query = query.replace('open', '')
            pyautogui.press('super')
            pyautogui.typewrite(query)
            pyautogui.sleep(0.5)
            pyautogui.press('enter')
            speak(engine, 'Opening ' + query)

        elif 'close this tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'new tab' in query:
            pyautogui.hotkey('ctrl', 't')

        elif 'change tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'go back' in query:
            pyautogui.hotkey('alt', 'left')

        elif 'search about' in query or 'search for' in query:
            speak(engine, "Sure sir")
            cm = query.replace('search about', '').replace('search for', '')
            pyautogui.hotkey('ctrl', 'k')
            pyautogui.typewrite(cm)
            pyautogui.press('enter')
            speak(engine, 'Searching ' + cm)

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak(engine, "Sir, what should I play on YouTube?")
            cm = takeCommand()
            if 'nothing' not in cm and cm != "None":
                # Ensure pywhatkit is installed; if not, install it via pip
                import pywhatkit as kit
                kit.playonyt(cm)

        elif 'open youtube' in query:
            speak(engine, "Sir, what should I play on YouTube?")
            cm = takeCommand()
            if cm != "None":
                import pywhatkit as kit
                kit.playonyt(cm)

        elif 'close youtube' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com")

        elif 'open spotify' in query:
            os.system("start spotify")

        elif 'close spotify' in query:
            os.system("taskkill /f /im spotify.exe")

        elif 'open google' in query:
            speak(engine, "Sir, what should I search on Google?")
            search_query = takeCommand()
            if search_query != "None":
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(engine, joke)

        elif "temperature" in query:
            search = "temperature in Dehradun"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(engine, f"Current {search} is {temp}")

        elif "where am i" in query or "where are we" in query:
            speak(engine, "Wait sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data.get('city', 'unknown')
                country = geo_data.get('country', 'unknown')
                speak(engine, f"Sir, I think we are in {city} city of {country} country")
            except Exception as e:
                speak(engine, "Sorry sir, due to a network issue I am not able to find where we are.")

        elif 'you can sleep' in query or 'sleep now' in query:
            speak(engine, "Okay sir, I am going to sleep. You can call me anytime.")
            break

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            engine = initialize_voice()
            speak(engine, "Thanks for using me sir, have a good day.")
            sys.exit()
