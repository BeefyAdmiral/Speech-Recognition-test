import speech_recognition as sr
from playsound import playsound

# Building the recognizer model
r = sr.Recognizer()

# Check if command was given
is_command_given = False

# Using Google API to identify the text
with sr.Microphone() as source:
    
    # Adjust for ambient noise before recognition
    r.adjust_for_ambient_noise(source)
    print("Setup complete")
    
    # read the audio data from the default microphone
    while is_command_given == False:
        audio_data = r.listen(source)
        print("Recognizing...")
        
        # Standing by till user speaks a specific word. In this case - "Hello"
        try:
            text = r.recognize_google(audio_data)
            text = text.split()
            
            # Confirming the word and alerting the user
            if "hello" in text:
                playsound('notification.mp3')
                command = r.listen(source)
                req = r.recognize_google(command)
                
                # After response is received print the response and close the
                # program
                print(req)
                is_command_given = True
                
        # If user taking too long then stand-by for a response
        except:
            print("Failed!")
            is_command_given = False
