

import webbrowser
from datetime import datetime



def speak(text):
    print("Assistant:", text)


while True:
    command = input("Enter command: ").lower()

    if "hello" in command:
        speak("Hello! How are you?")

    elif "time" in command:
        speak(datetime.now().strftime("%I:%M %p"))

    elif "google" in command:
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command:
        speak("Goodbye!")
        break
