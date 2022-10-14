"""
    Setup preparation
    ==================

    pip3 install pyttsx3
    python.exe --version
        ==>Python 3.9.7
    python.exe -c "import struct;print(struct.calcsize('P') * 8)"
        ==>64
 
    May not be needed at all - need to validate !!!
            Microsoft Visual C++ 14.0 or greater is required. 
            Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
            ==>Download Build Tools 
                -->Run the Visual Studio Installer(12.99 MB) 
                -->Select "MSVC v140 - VS 2015 C++ build tools (v14.00)"
                -->It will also download Windows Universal CRT SDK
            Total download size 819 MB. Total install size 3.58 GB.
            After installation it will reflect as "Visual Studio Build Tools 2022"
        

    pip3 install SpeechRecognition
    pip3 install pyjokes



"""



import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understanding")



data = sptext()

def speechttxt(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',110)
    engine.say(x)
    engine.runAndWait()


speechttxt(data)

