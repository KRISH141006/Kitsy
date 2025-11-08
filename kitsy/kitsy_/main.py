import speech_recognition as sr
import pyaudio
import os
import pyttsx3 as tts
import heeraConfig as hc


if __name__ == "__main__" :

    while True:
        r = sr.Recognizer()
        hc.speak("what can I do for you?")

        try:
            with sr.Microphone() as mic :
                print("listening...")
                audio = r.record(mic,duration=4)
                print("recognizing...")
                text = r.recognize_google(audio)
                text = text.lower()

                print("you said : " , text , sep = "\n")
                if "shutdown" in text or "shut down" :
                    hc.speak("shutting down the system")
                    os.system("shutdown /s /f /t 0")
                elif "restart" in text or "re start":
                    hc.speak("restarting the system")
                    os.system("shutdown /r /f /t 0")
                elif "log off" in text or "logout" in text or "log out" in text or "logoff":
                    hc.speak("signing off")
                    os.system("shutdown /l")
                else :
                    hc.speak("can you speak again?")


        except Exception as e:
            print("Error; {0}".format(e))


