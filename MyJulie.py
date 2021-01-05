import pyttsx3  # text to speach
import os
import datetime
import speech_recognition as sr  # used google speech api
import wikipedia  # To search my required info
import webbrowser  # browse

engine = pyttsx3.init()#initialize default for windows sapi5,for mac nsss --drivers
voices = engine.getProperty('voices')

print(voices[1].id)  # Zaira

engine.setProperty('voice', voices[1].id)  # set zaira's voice

# audio = strings given. say will only run after runandWait
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # get current time
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Raahul bhai !!how can I help u")


def takeCommand():
    # takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:  # aliasing as source
        print("Listening......")
        r.pause_threshold = 1  # Listening Wait time
        audio = r.listen(source)  # source=Microphone

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')  # use google api set language to english--version indian
        print(f"User said: ,{query}\n")

    except Exception as e:
        print(e)

        print("Please repeat again..")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()  # convert all command(str) to lower

    # logic for executing tasks
    if True:
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            # returns the first n provided sentences after search from page
            results = wikipedia.summary(query, sentences=6)
            speak("According to Wikipedia")
            print(results)  # print the strings returned
            speak(results)  # speak reads the string passed to it
            speak("For more info go to wikipedia.com")

        elif 'open youtube' in query:
            speak("Please wait Bhai!!opening youTube......")
            webbrowser.open("youtube.com")
            pass

        elif 'open google' in query:
            speak("Please wait Bhai!!opening google......")
            webbrowser.open("google.com")
            pass

        elif 'open stack overflow' in query:
            speak("Please wait Bhai!!opening stackoverflow......")
            webbrowser.open("stackoverflow.com")
            pass

        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"The time is {startTime}")
            pass

        elif 'open visual studio' in query:
            speak("Please wait Bhai!!opening your VS Code......")
            codepath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)  # open the file.exe
            pass

        elif 'who is your boss' in query:
            speak("Bhai!!! , Rahul bhai is always my boss and I am happy to help him")
            pass

        elif 'open rahul bhai ka game' in query:
            speak("Launching your game Bhai!!Please wait!!!")
            mygamepath = "C:\\Program Files (x86)\\Dragon(Windows)\\Dragon.exe"
            os.startfile(mygamepath)
            pass

        elif 'open github profile' in query:
            speak("Please wait Bhai!!opening your github Profile......")
            webbrowser.open("github.com/rahulshastryd")
            pass

        elif 'thank you' in query:
            speak("Welcome Raahul Bhai , Its my pleasure to help you!!!")
            pass

        elif 'open game art' in query:
            speak("Please wait Bhai , opening gamearts......")
            webbrowser.open("opengameart.org")
            pass

        elif 'open my game site' in query:
            speak("Please wait Bhai , opening your game site......")
            webbrowser.open(
                "https://gamedevrs065.itch.io/the-lost-world-of-dragon-pc")
            pass

        elif 'what is your name' in query:
            speak(
                "My name is Julie , always loyal and in service virtually to my boss Rahul Bhai . ")
            pass

        else:
            pass
