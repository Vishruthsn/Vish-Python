import speech_recognition as sr

AUDIO_FILE = ("example.wav")

#use the audio file as the audio source

r = sr.Recognizer()

with sr.Microphone() as source:
		#read the audio file. Here we use record insted of
		#listen
		audio = r.record(source)

try:
	print("The audio file contains:" + r.recognize_google(audio))

except sr. UnknownValueError:
	print("Google Speech Recognition could not understand audio")

except sr. RequestError as e:
	print("could not request results from Google Speech Recognition service; {0}". format)   