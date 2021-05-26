import os
import pyttsx3
import speech_recognition as sr
import psutil
from Processes import Processes


class bot:
    def takeCommand(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 0.7
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                Query = recognizer.recognize_google(audio, language='en-in')
                print('The Query is ', Query)
            except Exception as e:
                print(e)
                print("Say that again...")
                return None
        return Query

    def speak(self, audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def quitSelf(self):
        process = Processes()
        self.speak('What do you want sir ?')
        take = self.takeCommand()
        while take is None:
            self.speak("i can not recognize your speech")
            print('i can not recognize your speech')
            take = self.takeCommand()
        if 'shut down' in take:
            process.shutdown()
        elif 'restart' in take:
            process.restart()
        elif 'search' in take:
            self.speak('What do you want me to search on?')
            take_command = self.takeCommand()
            process.searchOnGoogle(take_command)
        else:
            process.openApplication(take)


if __name__ == '__main__':
    while True:
        firstBot = bot()
        firstBot.quitSelf()

