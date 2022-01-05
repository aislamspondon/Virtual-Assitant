import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
work = True
def intro():
    engine.say("Hello Asraful, I'm Assistant, How can i help you ")
    engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    work = True
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant','')
                print(command)
            else:
                work=False
    except:
        pass
    return command

def run_vr():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'info' in command:
        #  or 'wikipedia' or 'who is' or 'tell me about' or 'tell me' or 'who the heck is'
        # person = command.replace('who is','')
        person = command.replace('info','')
        # person = command.replace('wikipedia','')
        # person = command.replace('tell me about','')
        # person = command.replace('tell me','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'date' in command:
        excuse = ["I have a headach","I'm not interested","I don't have a time","Can we go Latter","Not today","I'm not single","I have a boyfriend"]
        int_excuse = random.randrange(0,len(excuse))
        talk("Sorry, "+excuse[int_excuse])
    elif 'are you single' in command:
        excuse=["Sorry, I have a boyfriend","Sorry I'm in a relationship","Sorry I'm connecting with wifi","Sorry Not Interested","Yes I'm Single"]
        int_excuse = random.randrange(0,len(excuse))
        talk(excuse[int_excuse])
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk("Thank you ! Have a Good Time with me Asraful")
        work = False

    else:
        talk("I'm Sorry I don't know your Answer . ")


intro()
while work:
    run_vr()