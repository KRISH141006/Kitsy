import speech_recognition as sr
import pyaudio
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for v in voices:
    if "Heera" in v.name:
        engine.setProperty('voice', v.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as mic :
    print("Speak for 5 Seconds")
    print("recording...")
    audio = r.record(mic,duration=5)
    print("completed")

try : 
    text = r.recognize_google(audio)
    print("you said : " , text , sep = "\n")

except sr.UnknownValueError : 
    print("Try again !")
except sr.RequestError as e : 
    print(f"You got an error : {e}")

speak(text)

