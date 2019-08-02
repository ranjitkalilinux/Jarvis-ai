import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
engain = pyttsx3.init('sapi5')
voices = engain.getProperty('voices')
engain.setProperty('voice', voices[0].id)
def speak(audio):
    engain.say(audio)
    engain.runAndWait()
speak("hellow sir i am jarvis")
def wishme():
    hour = int(datetime.datetime.now().hour)
    date = datetime.datetime.now().date()
    if(hour>=0 and hour<12):
        speak("good morning sir")
        speak(f"the date is {date}")
    elif(hour<=12 and hour<18):
        speak("good afternoon")
        speak(f"date is {date}")
    else:
        speak("good evening sir\n")
        speak(f" sir the date is {date}")
def runcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
    try:
        print("Recornizing")
        query = r.recognize_google(audio, language='in-en')
        print(query)
    except Exception as E:
        print('tyr again')
        return "none"
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query = runcommand().lower()
        if "wikipedia" in query:
            speak("searching sir..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open stack" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "play song" in query:
            parrot = 'C:\\Users\\ranjit\\Videos'
            kali = os.listdir(parrot)
            os.startfile(parrot, kali[0])
        elif "open code" in query:
            speak("opening code")
            os.system("code")
            quit()
        elif "open js" in query:
            speak("opening sir")
            os.system("js")
            quit()
        elif "close code" in query:
            speak("closeing sir")
            os.system("taskkill  /F /IM code.exe")
        elif "close js" in query:
            speak("closing js sir")
            os.system("taskkill  /F /IM cmd.exe")



