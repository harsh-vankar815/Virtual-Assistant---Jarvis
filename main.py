import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = 'ENTER_YOUR_API_KEY'

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://youtube.com')
    elif 'open instagram' in c.lower():
        webbrowser.open('https://instagram.com')
    elif 'open facebook' in c.lower():
        webbrowser.open('https://facebook.com')
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the json response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headling
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the requests
        pass



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        
        print("recognizing...")
        # Recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == 'jarvis'):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {}".format(e))