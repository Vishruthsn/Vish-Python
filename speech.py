import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=5)
	print("Say Something!")
	while True:#creating a while loop
		audio = r.listen(source)#listening to microphone
		print("you said" + r.recognize_google(audio))#print output