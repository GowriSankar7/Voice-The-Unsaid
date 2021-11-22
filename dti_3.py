import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak:")
    audio = r.listen(source)

try:
    txt = r.recognize_google(audio)
    print("YOU SAID:",txt)
except sr.UnknownValueError:
    print("NOT UNDERSTOOD:")
except sr.RequestError as e:
    print("COULNT REQUEST RESULTS; (0)".format(e))


!pip install pybraille
from pybraille import convertText
# text = input()
print(convertText(txt))


import pyttsx3
text_speech = pyttsx3.init()
txt = input("enter that needs to be converted to speech")
text_speech.say(txt)
text_speech.runAndWait()


!pip install pybraille
from pybraille import convertText
# txt= input()
print(convertText(txt))
