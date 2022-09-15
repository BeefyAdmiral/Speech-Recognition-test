import speech_recognition as sr
from playsound import playsound

# Building the recognizer model
r = sr.Recognizer()

# Check if command was given
is_command_given = False

# Using Google API to identify the text
with sr.Microphone() as source:
    # read the audio data from the default microphone
    while is_command_given == False:
        audio_data = r.listen(source)
        print("Recognizing...")
    # convert speech to text
        try:
            text = r.recognize_google(audio_data)
            print(text)
            is_command_given == True
            break
    # If user taking too long then stand-by for a response
        except:
            print("Failed!")
            is_command_given = False
