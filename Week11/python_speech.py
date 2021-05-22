import os
import pyttsx3
import webbrowser
import speech_recognition as sr

# Hardware - Driver Programs ->  OS  -> Application 

class PythonHub:
	def takeCommands(self):
		# Using Recognizer and Microphone methods for input voice commands
		r = sr.Recognizer()

		with sr.Microphone() as source:
			print("Listening..")
			# Number of seconds of non-speaking audio before a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)
			# Voice input is identified
			query = None
			
			try:
				# listening voice commands
				print("Recognising..")
				query = r.recognize_google(audio, language='en-in')

				# Displaying voice command
				print("Query : '%s'" %(query))
			except Exception as ex:
				# Display exception
				print(ex)
				print("Please say again..")

			return query

	def speak(self, audio):
		# Method for voice output
		# engine = pyttsx3.init('sapi5')
		engine = pyttsx3.init()
		# setting voice type and id
		voices = engine.getProperty('voices')
		engine.setProperty('voice', 'english')
		engine.say(audio)
		engine.runAndWait()

	def searchOnline(self):
		self.speak("What do you want to search about?")
		searchQuery = self.takeCommands()
		if searchQuery is not None:
			url = "https://www.google.com.tr/search?q={}".format(searchQuery)
			webbrowser.open_new_tab(url)
		else:
			self.speak("Sorry. Could you please come again.")


if __name__ == '__main__':
	jarvis = PythonHub()
	jarvis.speak("Welcome back.")
	jarvis.searchOnline()