#speech recognition program

import speech_recognition as sr

r = sr.Recognizer()
#recognizer class to get audio from system

def listen():
    '''
    this loop for listning voice commands
    '''
    with sr.Microphone() as source:
        print("listining....")
        text = r.listen(source)
        r.pause_threshold= 1
        try:
            recognized_text = r.recognize_google(text ,language="en-in")
            return(recognized_text)
        except sr.UnknownValueError:
            return("Error")
        except sr.RequestError as e:
            return("Request Error")

lis = listen()
print(lis)
