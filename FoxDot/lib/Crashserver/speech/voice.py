# coding: utf8
#!/usr/bin/env python3

import os # Allows checking if using Windows
from threading import Thread 
import pythoncom
import comtypes.client  # Importing comtypes.client will make the gen subpackage
import time

try:
    from comtypes.gen import SpeechLib  # comtypes
except ImportError:
    # Generate the SpeechLib lib and any associated files
    engine = comtypes.client.CreateObject("SAPI.SpVoice")
    stream = comtypes.client.CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib

try:
	assert(os.name == 'nt') # Checks for Windows
except:
	raise RuntimeError("Windows is required.")


class Voix(Thread):
	""" CRASH SERVER - TEXT 2 SPEECH
		A text to speech thread using the Microsoft SAPI through COM
		Foxdot implantation
		"""

	def __init__(self, text="", rate=0.5, amp=1.0, voix=0, lang=""):
		Thread.__init__(self)
		pythoncom.CoInitialize()
		self.voice = comtypes.client.CreateObject('Sapi.SpVoice')
		self.voice_win = ["Hortense", "Zira", "David"]
		self.text = str(text)
		self.rate = float(rate)
		self.amp = float(amp)
		self.voix = voix
		self.lang = lang
		self.main()
		self.thread = Thread(target=self.say, kwargs={'text': self.text})
		self.thread.start()
		
	def main(self):
		self.set_rate(self.rate)  # Speed of speech
		self.set_amp(self.amp)    # Volume 
		self.set_voice(self.voix) # This is the VOICE 

	def initi(self, lieu=""):
		self.lieu = lieu
		self.crash_text_path = self.select_lang(self.lang) # return the .txt EN/FR/NL/... 
		self.crash_text = self.text_as_list(self.crash_text_path) # return the text as a list	
		self.set_voice(self.voix)
		print(self.crash_text)
		self.say(self.text_init)

	def intro(self):
		self.say(self.crash_text)	

	def select_lang(self, lang, lieu=""):
		"""Select the .txt according to language selected"""
		crash_text = ""
		if lang == "fr":
			crash_text = "crash_text_fr.txt"
			self.text_init = "Le Serveur {} est initialisé à {} heures, \
				{} minutes, et {} secondes.".format(self.lieu, str(time.strftime("%H")), str(time.strftime("%M")), str(time.strftime("%S")))
		if lang == "eng":
			crash_text = "crash_text_eng.txt"
			self.text_init = "The Server {} is initialized at {} hours, \
				{} minutes, and {} seconds".format(self.lieu, str(time.strftime("%H")), str(time.strftime("%M")), str(time.strftime("%S")))
			
		return os.path.join(os.getcwd(), "FoxDot", "lib", "Crashserver", "speech", crash_text)	
		#return os.path.join(os.getcwd(), crash_text)

	def text_as_list(self, text_path):
		""" Transform a .txt file into a list for each line""" 
		text_list = []
		with open(text_path, 'r', encoding='utf-8') as text:  
			line = text.readline()
			while line:
				text_list.append(line.rstrip('\n'))
				line = text.readline()
			return text_list

	def get_text_length(self):
		"""return the number of line, use in FoxDot"""
		length = len(self.crash_text)
		return length

	def say(self, text):
		""" Say the text """
		pythoncom.CoInitialize()
		#self.voice = wincl.Dispatch(pythoncom.CoGetInterfaceAndReleaseStream(self.voice_id, pythoncom.IID_IDispatch))
		if text is not None:
			self.voice.Speak(str(text))
			return
		else:
			self.stop()

	def stop(self):
		pythoncom.CoInitialize()
		self.thread.join()

	def set_rate(self, rate):
		"""Set the speed of the speaker -10 is slowest, 10 is fastest"""
		self.voice.Rate = int((self.rate*20) - 10)

	def set_amp(self, amp):
		"""Set the volume of the speaker"""
		self.voice.Volume = int(self.amp*100)

	def _create_stream(self, filename):
		"""Create a file stream handler"""
		stream = comtypes.client.CreateObject('Sapi.SpFileStream')
		stream.Open(filename, SpeechLib.SSFMCreateForWrite)
		return stream

	def get_voices(self, name=''):
		"""Get a list of voices, search by name optional"""
		voice_list = []
		voices = self.voice.GetVoices()

		if name is not '':
			for voice in voices:
				if name in voice.GetDescription():
					voice_list.append(voice)
					break
			else:
				print('Voice not found')
		else:
			for voice in voices:
				voice_list.append(voice)
		return voice_list

	def get_voice_names(self):
		"""Get the names of all the voices"""
		return [voice.GetDescription() for voice in self.get_voices()]

	def set_voice(self, voix):
		"""Set the voice to the given voice"""
		if self.lang == "fr":
			self.voix = 0
		if self.lang == "eng":
			self.voix = 1	
		self.voice.Voice = self.get_voices(self.voice_win[self.voix])[0]
		return

	def get_audio_outputs(self, name=''):
		"""Get the audio outputs, search for the one with the name if given"""
		output_list = []
		outputs = self.voice.GetAudioOutputs()

		if name is not '':
			for output in outputs:
				if name in output.GetDescription():
					output_list.append(output)
					break
			else:
				print('Audio output not found')
		else:
			for output in outputs:
				output_list.append(output)

		return output_list

	def get_audio_output_names(self):
		"""Get the names of all the audio outpus"""
		return [output.GetDescription() for output in self.get_audio_outputs()]

	def set_audio_output(self, output):
		if type(output) is str:
			self.voice.AudioOutput = self.get_audio_outputs(output)[0]
		else:
			self.voice.AudioOutput = output
		return

	def record(self, filename, message):
		"""Make a recording of the given message to the file
		The file should be a .wav as the output is
		PCM 22050 Hz 16 bit, Little endianness, Signed"""
		stream = self._create_stream(filename)
		temp_stream = self.voice.AudioOutputStream
		self.voice.AudioOutputStream = stream
		self.say(message)
		self.voice.AudioOutputStream = temp_stream



if __name__ == '__main__':
	v = Voix(lang="eng")
	v.initi("de la maison")