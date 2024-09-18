import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import subprocess
from googlesearch import search

engine = pyttsx3.init()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print("User said:"+query)
            return query
        except Exception as e:
            return "Did not recognize"


if __name__ == "__main__":
    engine.say("hello i am your assistant")
    engine.runAndWait()
    while True:
        print("Listening...")
        query = takecommand()
        #engine.say(query)

        #searching sites
        sites = [["google","https://www.google.com/"],["youtube","https://www.youtube.com/"],]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                engine.say(f"opening  {site[0]} sir ")
                webbrowser.open(site[0])
                engine.runAndWait()
        #time
        if f"Time".lower() in query.lower():
            time = time.strftime("%I:%M %p")
            engine.setProperty('rate', 150)
            engine.say(f"Sir the time is {time}")
            engine.runAndWait()
       
       #app opening
        apps = [["my",r"C:\Users\jewel\Desktop\My"],]

        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                engine.say(f"opening  {app[0]} sir ")
                subprocess.call(app[1])
                engine.runAndWait()

        #web searching
        if f"search".lower() in query.lower():             
            query1 = query
            
            for j in search(query1, tld="co.in", num=1, stop=1):
                print(j)
                webbrowser.open(j)

            
            