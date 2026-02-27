import speech_recognition as sr
import webbrowser
import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing.......")
    while True:
      r = sr.Recognizer()
      with sr.Microphone() as source:
         print("Listening.....")
         audio = r.listen(source)

    #Recognize speech using sphinx
      try:
         command = r.recognize_google(audio)
         print(command) 
      except sr.UnknownValueError:
         print("Sphinx could not listen audio")
      except sr.RequestError as e:
         print("Sphinx error; {0}".format(e))
