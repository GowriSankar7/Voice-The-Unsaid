
import pyttsx3
text_speech = pyttsx3.init()
answer = input("enter that needs to be converted to speech")
text_speech.say(answer)
text_speech.runAndWait()
