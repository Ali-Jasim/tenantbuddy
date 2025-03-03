import os

import speech_recognition as sr

os.system('cls')

# obtain audio from the microphone


r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)

#clear the terminal after listening
        os.system('cls')

        print("Recognizing...")

        try:
            # recognize speech using Whisper
            print("Whisper thinks you said " + r.recognize_whisper(audio, language="english", model="tiny.en"))
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Whisper; {e}")


