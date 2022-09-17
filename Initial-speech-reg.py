import logging
import threading
import time
import concurrent.futures
import speech_recognition as sr
from playsound import playsound


def thread_function(name):
    # Using Google API to identify the text
    with sr.Microphone() as source:
    
        # Adjust for ambient noise before recognition
        r.adjust_for_ambient_noise(source)
        print("Setup complete")
        
        while True:
            print("running")
            if len(found) != 0:
                break
            else:
                audio_data.append(r.listen(source))
                print("test")

def thread_function2(name):
    while True:
        if len(audio_data) != 0:
            t = audio_data.pop(0)
            text = r.recognize_google(t)
            text = text.split()
            print(text)
            if "hello" in text:
                found.append(1)
                print("found")
                break
            
    playsound('notification.mp3')
    is_command_given = False
    
    with sr.Microphone() as source:
        # Wait for the command
        while is_command_given == False:
            print(is_command_given)
            command = r.listen(source)
            print("Recognizing...")
        
            # Standing by till user speaks a specific word. In this case - "Hello"
            try:
                text = r.recognize_google(command)
                is_command_given = True
                # After response is received print the response and close the
                # program
                print(text)
                
            # If user taking too long then stand-by for a response
            except:
                print("Failed!")
                is_command_given = False
            

# Building the recognizer model
r = sr.Recognizer()

# Variables to store the audio data and specific text found
audio_data = []
found = []

# Creating 2 threads, one to listen to audio source and other to detect the 
# initial response
x = threading.Thread(target=thread_function, args=(1,))
y = threading.Thread(target=thread_function2, args=(1,))
    
x.start()
y.start()
