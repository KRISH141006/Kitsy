import pyttsx3 as tts

heera = tts.init() # initialising pyttsx3 module 

def speak(text):
    heera.__init__()
    voices = heera.getProperty('voices')
    for v in voices :
        if 'Heera' in v.name :
            heera.setProperty('voice',v.id)
            # print('done with changing voice')
            break
    heera.say(text)
    heera.runAndWait()
    heera.stop()

if __name__ == "__main__" :
    speak("hello")