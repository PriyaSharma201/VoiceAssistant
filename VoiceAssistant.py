import speech_recognition as sr 
import webbrowser 
import datetime 
import psutil
import os
import pyjokes
import pyautogui
import wikipedia 
import pyttsx3
import time 
import phonenumbers 
from phonenumbers import geocoder, timezone,carrier 
import pytube
from pywhatkit import sendwhatmsg_instantly 




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',140) 
                   
                   

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")


        audio = r.listen(source)
        speak("listening...")

    try:
        print("recoginising...")
        query = r.recognize_google(audio,language="en")
    except:
        speak("I did not get that...")
        return 'none'
    return query
    

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print(f"Good morning")
        speak(f"Good morning")
    elif hour >= 12 and hour < 16:
        print(f"Good afternoon ")
        speak(f"Good afternoon")
    else:
        print(f"Good evening")
        speak(f"Good evening")

wishme()
speak("I am Emo, please tell how may I help you")  


while True:
    query = takecommand().lower()
    if "hello" in query:
        print("hello dear")
        speak("hello dear")
    elif "exit" in query:
        print("ok i am going offline")
        speak("ok i am going offline")
        exit()
    elif "open google" in query:
        print("opening google...")
        speak("opening google...")
        webbrowser.open("http://www.google.com")
    elif "open facebook" in query:
        print("opening facebook...")
        speak("opening facebook...")
        webbrowser.open("http://www.facebook.com")
    elif "open youtube" in query:
        print("opening youtube...")
        speak("opening youtube...")
        webbrowser.open("http://www.youtube.com") 
    elif "open instagram" in query:
        print("opening instagram...")
        speak("opening instagram...")
        webbrowser.open("http://www.instagram.com")   
    elif 'open notepad' in query:
            print("Opening Notepad...")
            speak("Opening Notepad...")
            os.startfile("c:\\Windows\\System32\\notepad.exe")
            speak("Write it down")
            a = takecommand()
            pyautogui.typewrite(a)
    elif "write it down" in query:
        print("Tell me what do you want to write...")
        speak("Tell me what do you want to write...")
        query = takecommand()
        pyautogui.typewrite(query,1)
    elif 'battery' in query:
        print(f"battery is {psutil.sensors_battery().percent}")
        speak(f"battery is {psutil.sensors_battery().percent}")
    elif 'volume up' in query:
            speak("Increasing volume...")
            pyautogui.press('volumeup')
    elif 'volume down' in query:
            speak("Decreasing volume...")
            pyautogui.press('volumedown')
    elif 'volume mute' in query:
        print("ok volume mute")
        speak("ok volume mute")
        pyautogui.press("volumemute")
    elif 'volume unmute' in query:
        print("ok volume unmute")
        speak("ok volume unmute")
        pyautogui.press("volumeup")
    elif 'wikipedia' in query:
        print("searching wikipedia")
        speak("searching wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 3)
        print(results)
        speak(results)
    elif 'time' in query:
        print(f"The Time is {time.strftime('%H : %M : %S : %p')}")
        speak(f"The Time is {time.strftime('%H : %M : %S : %p')}")

    elif 'send message' in query:
        print("Tell me the message you want to send...")
        speak("Tell me the message you want to send...")
        message = takecommand().lower()
        print("Tell me the message you want to send...")
        speak("Tell me the message you want to send...")
        number = input("Enter Number :")
        sendwhatmsg_instantly(number,message,10)
    
    elif 'open map' in query:
        print("opening map...")
        speak("opening map...")
        webbrowser.open("https://www.google.com/maps/")
    elif 'where am i' in query:
        print("Finding your location...")
        speak("Finding your location...")
        webbrowser.open("https://www.google.com/maps/@")
    elif 'number details' in query:
        print("Tell me the number you want to search...")
        speak("Tell me the number you want to search...")
        speak("Enter the number")
        number = input("Enter the number:")
        print("Searching number details...")
        speak("Searching number details...")
        num = phonenumbers.parse(number)
        print(f"Country is {geocoder.country_name_for_number(num,'en')}")
        speak(f"Country is {geocoder.country_name_for_number(num,'en')}")
        print(f"Carrier Name is {carrier.name_for_number(num,'en')}")
        speak(f"Carrier Name is {carrier.name_for_number(num,'en')}")
    elif 'convert youtube to mp3' in query:
        print("Enter the video link you want to convert...")
        speak("Enter the video link you want to convert...")
        link = "https://youtube.com/"
        video = pytube.YouTube(link)
        print("Converting video to mp3...")
        speak("Converting video to mp3...")
        music = video.streams.filter(only_audio=True).first().download()
        new_path = os.path.split(music)
        os.rename(music,new_path[0]+".mp3")
        print("conversion completed...")
        speak("conversion completed...")
    elif 'open visual studio code' in query:
            speak("Opening Visual Studio Code...")
            file_name = input("Enter the file name with extension: ")
            if os.path.isfile(file_name):
                os.startfile(file_name)
                speak("File opened. You can start writing.")
            else:
                speak("File not found. Please check the file name and try again.")
    elif "screenshot" in query:
            speak("Taking a screenshot...")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved as screenshot.png.")  
    elif 'jokes' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)