import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests


engine = pyttsx3.init()
newsapi = "0a481e62177f487698f3378090473c8a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
      webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = music.music[song]
       webbrowser.open(link)
    elif "news" in c.lower():
       r = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2026-01-27&sortBy=publishedAt&apiKey={newsapi}")
       if r.status_code==200:
          data = r.json()
          articles=data.get('articles',[])
          for article in articles:
             speak(article['title'])
    else:
       pass


if __name__ == "__main__":
    speak("Initializing.......")
    while True:
    #Recognize speech using sphinx
      try:
         r = sr.Recognizer()
         with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
         print("Recognizing....")
         command = r.recognize_google(audio)
         if(command.lower() == "jarvis"):
            speak("Ya")
            with sr.Microphone() as source:
               print("jarvis Active....")
               audio = r.listen(source)
               command = r.recognize_google(audio)

               processcommand(command)

      except Exception as e:
         print("Error; {0}".format(e))
