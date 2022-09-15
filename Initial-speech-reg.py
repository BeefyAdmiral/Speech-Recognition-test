import sounddevice as sd
import wavio
import speech_recognition as sr

# output file name
filename = 'output.wav'

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

# Record for 3 seconds
print("Start speaking!")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

# Saving the output file produced during the run time
wavio.write(filename, myrecording, fs ,sampwidth=2)

# Building the recognizer model
r = sr.Recognizer()

# Using Google API to identify the text
with sr.AudioFile(filename) as source:
    data = r.record(source)
    text = r.recognize_google(data)
print(text)
