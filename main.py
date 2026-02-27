import speech_recognition as sr
import webbrowser
import pyttsx3
import music


engine = pyttsx3.init()

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
