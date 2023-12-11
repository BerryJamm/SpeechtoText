# Python program to translate speech to text and text to speech
import webbrowser

import pyttsx3
import speech_recognition as sr

recognize = sr.Recognizer()


def speaktext(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while 1:
    try:
        with sr.Microphone() as source2:
            recognize.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = recognize.listen(source2)
            MyText = recognize.recognize_google(audio2).split()
            if "stop" in MyText:
                speaktext("Bye! See you later.")
            elif "hello" in MyText:
                speaktext("Hello! Hope you are doing well today!")
            elif "yes" in MyText:
                speaktext("I'm glad I got that right.")
            elif "no" in MyText:
                speaktext("Sorry I missed that.")
            elif "music" in MyText:
                speaktext("Opening Spotify. Generating music for you.")
                webbrowser.open("https://open.spotify.com/")
            else:
                MyText = str(MyText).lower()
                print(f"Did you say, {MyText}")

    except sr.RequestError as e:
        print(f"Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
