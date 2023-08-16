# Go to - https://pypi.org/project/SpeechRecognition/ - and copy and paste it in the terminal
# Go to - https://pypi.org/project/pyttsx3/ -  and copy and paste it in the terminal
# Go to - https://pypi.org/project/PyAudio/ - and copy and paste it in the terminal
#Go to  - https://pypi.org/project/pywhatkit/ - and copy and paste it in the terminal
#Go to - https://pypi.org/project/wikipedia/ -  and copy and paste it in the terminal
#Go to - https://pypi.org/project/pyjokes/ - and copy and paste it in the terminal

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexis" in command:
                command = command.replace("alexis", "")
    except:
        pass
        return command

def run_alexis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f"The current time is {time}")
    elif "wiki" in command:
        question = command.replace("wiki", "")
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)
    elif "date" in command:
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        print(date)
        talk(f"Today is {date}")
    elif "joke" in command:
        joke = (pyjokes.get_joke())
        print(joke)
        talk(joke)
    else:
        print("Please say that again")
        talk("Please say that again")

while True:
    run_alexis()



