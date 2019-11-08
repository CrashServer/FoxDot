# coding: utf8
#!/usr/bin/env python3

import os 
import sys
from threading import Thread 
import time
from ...Settings import FOXDOT_ROOT
try:
	import pyttsx3
except:
	print("Please install pyttsx3, with pip install pyttsx3")


class Voice(Thread):
	""" Text 2 Speech"""
	def __init__(self, text="", rate=1, amp=1.0, lang="french", voice=1):
		Thread.__init__(self)
		self.engine = pyttsx3.init()
		self.text = str(text)
		self.rate = rate / 100
		self.amp = float(amp)
		self.lang = lang
		self.voice = voice
		self.thread = Thread(target=self.say, kwargs={'text': self.text})
		self.thread.start()
		
	def main(self):
		self.engine.setProperty('rate', self.rate)    # Speed percent (can go over 100)
		self.engine.setProperty('volume', self.amp)   # Volume (0 - 1) 
		
	def say(self, text):
		""" Say the text """
		#self.engine.stop()
		self.set_voice(self.lang, self.voice)
		self.main()		
		if text is not None:
			self.engine.say(str(text))
			self.engine.runAndWait()
		else:
			self.stop()

	def stop(self):
		self.engine.stop()
		if self.thread.isAlive():
			self.thread.join()

	def get_voices(self):
		"""Get a list of voices"""
		voices_list = self.engine.getProperty('voices')
		for voice in voices_list:
			print(" - ID: %s" % voice.id)
		return voices_list

	def set_voice(self, lang="", voice=1):
		"""Get the names of all the voices"""
		if self.voice < 1 or self.voice > 4:
			self.voice = 1
		langvoice = str((str(self.lang) + "+f" + str(self.voice))) 
		self.engine.setProperty('voice', langvoice)

class init_server():
	def __init__(self, lang="french", lieu="ici"):
		self.lang = lang
		self.lieu = lieu

	def initi(self):
		if self.lang == "french":
			self.text_init = "Le Serveur {} est initialisé à {} heures, \
				{} minutes, et {} secondes.".format(self.lieu, str(time.strftime("%H")), str(time.strftime("%M")), str(time.strftime("%S")))
		if self.lang == "english":
			self.text_init = "The Server {} is initialized at {} hours, \
				{} minutes, and {} seconds".format(self.lieu, str(time.strftime("%H")), str(time.strftime("%M")), str(time.strftime("%S")))
		return self.text_init

	def crash_txt(self):
		try: 
			self.crash_text_path = self.select_lang() # return the .txt EN/FR/NL/... 
			self.crash_text = self.text_as_list(self.crash_text_path) # return the text as a list	 
			return self.crash_text
		except:
			print("Error in crash_txt", sys.exc_info())

	def text_as_list(self, text_path):
		""" Transform a .txt file into a list for each line""" 
		text_list = []
		with open(text_path, 'r', encoding='utf-8') as text:  
			line = text.readline()
			while line:
				text_list.append(line.rstrip('\n'))
				line = text.readline()
			return text_list

	def select_lang(self):
		"""Select the .txt according to language selected"""
		try: 
			crash_text = ""
			if self.lang == "french":
				crash_text = "crash_text_fr.txt"
			if self.lang == "english":
				crash_text = "crash_text_eng.txt"	
			return os.path.join(FOXDOT_ROOT, "lib", "Crashserver", "speech", crash_text)	
			#return os.path.join(os.getcwd(), crash_text)
		except:
			print("Error select lang", sys.exc_info())

if __name__ == '__main__':
	#v = Voice("Bonjour, ça va tu bien", lang="french", voice=4)
	init_server().text_as_list("crash_text_fr.txt")
	
	#v.say("hello")
	#v.get_voices()

	
