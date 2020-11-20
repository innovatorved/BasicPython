#speech recognition program

import speech_recognition as sr

r = sr.Recognizer()
#recognizer class to get audio from system
def aud():
    with sr.Microphone() as source:
        print("Listining....")
        text = r.listen(source)
        r.pause_threshold = 1
        try:
            recognized_text = r.recognize_google(text)
            return(recognized_text)
        except sr.UnknownValueError:
            return("Error")
        except sr.RequestError as e:
            return("Request Error")
txt = aud()
print(txt)
