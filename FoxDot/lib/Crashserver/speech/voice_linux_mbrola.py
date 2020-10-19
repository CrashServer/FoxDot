# coding: utf8
#!/usr/bin/env python3

import os 
import sys
import time
import subprocess

from threading import Thread 

from ...Settings import FOXDOT_ROOT
from ..crash_conf import crash_path

class Voice(Thread):
	""" Text 2 Speech Linux Mbrola Mod
	"""
	def __init__(self, text="", rate=100, amp=1.0, lang="fr", voice=1, pitch=80, octave=0, gap=0, record = ""):
		Thread.__init__(self)
		self.text = str(text)
		if self.text=="":
			self.text = " "
		self.rate = rate
		self.amp = amp*100
		self.lang = lang
		self.voice = voice
		self.pitch = pitch
		self.octave = octave
		self.gap = gap
		self.record = record
		self.mbrola_voice = self.set_voice()
		self.thread = Thread(target=self.say, kwargs={'text': self.text})
		self.thread.start()
	
	def say(self, text, record=""):
		""" Say the text and possibility to record """
		espeak_cmd = self.create_cmd()
		subprocess.call(espeak_cmd)	
		#subprocess.call(["espeak", "-a", f"{self.amp}", "-g", f"{self.gap}" ,"-v", f"{self.mbrola_voice}", "-s", f"{self.rate}", "-p",f"{self.pitch}", f"{self.text}", "-w", f"{record_path}"])
		
	def create_cmd(self):
		""" Configure the espeak comd line """
		cmd = ["espeak"]
		cmd.extend(["-a", f"{self.amp}"]) # amp
		cmd.extend(["-g", f"{self.gap}"]) # gap
		cmd.extend(["-v", f"{self.mbrola_voice}"]) # voice (lang + voice + octave)
		cmd.extend(["-s", f"{self.rate}"]) # speed
		cmd.extend(["-p",f"{self.pitch}"]) # pitch
		cmd.extend([f"{self.text}"]) # text
		if self.record != "":
			record_path = os.path.join(crash_path, "_loop_", "voicetxt", f"{self.record}.wav")
			cmd.extend(["-w", f"{record_path}"]) # enable record
		return cmd	

	def stop(self):
		if self.thread.isAlive():
			self.thread.join()

	def get_voices(self):
		"""Get a list of voices"""
		proc = subprocess.Popen('espeak --voices=mbrola', shell=True, stdout=subprocess.PIPE)
		voices_list = proc.stdout.read()
		voices_list = voices_list.decode().splitlines()

		voices_dict = {}
		for i in range(1, len(voices_list)):
			language = voices_list[i].split()[4].split("mb/")[1]
			if len(language) == 6:
				language = language[3:-1]
				voice_index = voices_list[i].split()[4].split("mb/")[1][-1]
				if language in voices_dict:
					voices_dict[language].append(voice_index)
				else:
					voices_dict[language] = [voice_index]		
		return voices_dict

	def set_voice(self, lang="fr", voice=0, octave=0):
		"""set the voices"""
		voices_list = self.get_voices()
		if self.lang == "":
			print([v for v in voices_list.keys()])	
		else:
			if self.lang not in voices_list:
				self.lang = "fr"	
			if self.octave == 0:
				self.octave = ""
			else:
				self.octave = f'+{self.octave}'	
			if self.voice >= len(voices_list[self.lang]):
				self.voice = len(voices_list[self.lang]) - 1 
			mbrola_voice = f'mb-{self.lang}{voices_list[self.lang][self.voice]}{self.octave}'
			return mbrola_voice


class init_server():
	def __init__(self, lang="fr", lieu="ici"):
		self.lang = lang
		self.lieu = lieu

	def initi(self):
		if self.lang == "fr":
			self.text_init = "Hello world ? Le Serveur {} est initialisé à {} heures, \
				{} minutes, et {} secondes.".format(self.lieu, str(time.strftime("%H")), str(time.strftime("%M")), str(time.strftime("%S")))
		if self.lang.startswith("en"):
			self.text_init = "Initialisation. {} Server. At {} hours, \
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

	
