import pyttsx3
from datetime import *

# One time initialization
engine = pyttsx3.init()

voices = engine.getProperty('voices')
#print(voices)

# Set properties _before_ you add things to say
engine.setProperty('voice' , voices[0].id) #voice type
engine.setProperty('rate', 170)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1

'''
#details about voice 
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
'''
def today_date():
    wish = datetime.now().hour
    #print(wish)
    if wish >=0 and wish<12:
        speak("Gud Morning Sir")
    elif wish>=12 and wish<16:
        speak("Gud Afternoon Sir")
    elif wish>=16 and wish<=22:
        speak("Gud Evening Sir")
    else:
        speak("Gud Night Sir")
        
    today = date.today()
    #print(today.day)
    speak("Today Date is");
    speak("Today day is"+str(today.day))
    speak("month is" + str(today.month))
    speak("year is" + str(today.year))
    print(today)
    
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("my name is Next Innovation")
today_date()

