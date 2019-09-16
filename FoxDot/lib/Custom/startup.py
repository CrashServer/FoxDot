#coding: utf8
#!/usr/bin/env python3
#####  CRASH SERVER CUSTOM STARTUP ###########
import os
import sys
from .Settings import FOXDOT_ROOT
import pyperclip as clip
#  OPTIONAL ASCII GENERATOR
from pyfiglet import figlet_format

#########################
### SERVER CONFIG     ###
#########################

### Lieu du Server
lieu = str("du diamand d'or")
### Longueur mesure d'intro
tmps = 16
### Language
lang = "french"
voice = 0
### BPM intro
bpm_intro = 48
### Scale intro
scale_intro = "minor"
### Root intro
root_intro = "E"
### Video  
video = 0
adresse = "192.168.0.22"

### LOAD CUSTOM SYNTHDEFS #####
try:
	from .Crashserver.crashSynthDefs import * ### Crash Custom SynthDefs
	from .Crashserver.crashFX import * ### Crash Custom Fx
except:
	print("Error importing SynthDefs, FX or Loop player : ", sys.exc_info()[0])

### EXTENSIONS #######
### TXT 2 Speech ####
try:
	if sys.platform == "Windows":
		from .Crashserver.speech.voice import *   ### Text2Speech Windows
	elif sys.platform.startswith("linux"):
		from .Crashserver.speech.voice_linux import *   ### Text2Speech linux
	else:
		print("Txt2Speech don't work for ", sys.platform)
except:
	print("Error importing Speech Extension")

### Foxdot tools
try:	
	from .Crashserver.arpy import *
	from .Crashserver.sdur import *
	from .Chords import *
	#from .Crashserver.coolfunction import *
	# from .Extensions.timer.hack import * ### Crash Server Timer
	#from .Extensions.Video.video2 import *    ### Video player
except:
	print("Error importing Extensions : ", sys.exc_info())

### Code generator
try:
	from .Crashserver.weapons import *
except:
	print("Error in generating weapons code")

## Path Snd
crash_path = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_snd/")

try: 
	FOXDOT_SND   = crash_path
	FOXDOT_LOOP  = os.path.realpath(crash_path + "/_loop_/")
	FoxDotCode.use_sample_directory(FOXDOT_SND)
	Samples.addPath(FOXDOT_LOOP)
except:
	print("Error importing Custom Sound", sys.exc_info()[0])

# OSC VIDEO Filtered FORWARD
try:
	class FilterOSCClient(OSCClient):
			def send(self, message, *args):
					if "video" in str(message.message):
							OSCClient.send(self, message, *args)
	def OSCVideo(adresse):
		my_client = FilterOSCClient()
		my_client.connect((adresse, 12345))
		Server.forward = my_client
except:
	print("Error forwarding OSC to video", sys.exc_info()[0])

### Voice initialisation
def init_voice():
	if sys.platform.startswith("win"):
		voix = Voice(lang=lang, rate=0.45, amp=1.0)
		voix.initi(lieu)
		Clock.future(tmps, lambda: voix.intro())
	elif sys.platform.startswith("linux"):
		serv = init_server(lang, lieu)
		txt_init = serv.initi()
		crash_txt = serv.crash_txt()
		def txt_intro():
			Voice(crash_txt, rate=1, amp=1, lang=lang, voice=voice)
		Voice(txt_init, rate=1, amp=1, lang=lang, voice=voice)
		Clock.future(tmps, lambda: txt_intro())	
	else:
		print("Sorry, we crash only from windows or linux")

### LPF during Txt 2 Speech
def voice_lpf(freq=400):
	Master().lpf=freq

def calc_dur_voice(phrase=""):
	return (round((60/100)*len(phrase.split())*(Clock.bpm/60)))

### Generate ASCII from text into the clipboard 
def ascii_gen(text=""):
	if text is not None:
		clip.copy(figlet_format(text))

##############   BEGIN ##############################################


def connect(video=video):
	print(code["connect"][0])
	Clock.bpm = bpm_intro
	Scale.default = scale_intro
	Root.default = root_intro
	if video==1:
		OSCClient(adresse)
		vi >> video(vid=0, speed=1, vfx1=0, vfx2=0)		
	i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3], start=now), hpf=expvar([0,500],[tmps*6, tmps*2]))
	clip.copy(figlet_format(code["connect"][0]) + "\n\n\n" + code["connect"][2])


def attack(part="default"):
	if type(part) is not str:  ### so we can type attack(42) or attack(43)
		part = str(part)

	### Random choice of part
	elif part == "default":    
		part = choice([i for i in code.keys() if i not in ["init", "connect"]])
	
	### Define prompt
	exten = ''.join(choice(string.ascii_lowercase) for x in range(3))
	prompt = "# attack@{}.{}:~$ ".format(part, exten)
	
	### Init server
	if part == "init":    
		init_voice()
		clip.copy(figlet_format(code[part][0]) + "\n\n\n" + prompt + define_virus()+ "\n" + code[part][2])
	
	### Random code generator
	if part == "42" or part == "random":   ### Random Synth code
		clip.copy(prompt + define_virus()+ "\n" + random_virus())
	elif part=="43":  ### Random play code
		clip.copy(prompt + define_virus()+ "\n" + random_virus_char())
	
	### Select Part and generate Ascii text
	else:
		if code[part][2] and code[part][0] is not None:
			clip.copy(figlet_format(code[part][0]) + "\n\n\n" + prompt + define_virus()+ "\n" + code[part][2])
	
	### Generate Voice
	if code[part][1] is not None:   ### Voice generator
		voice_lpf(400)
		Voice(code[part][1], rate=1, lang=lang, voice=randint(1,5))		
		Clock.future(calc_dur_voice(code[part][1]), lambda: voice_lpf(0))

################# END #################################################

def lost():
	print([i for i in code.keys()])


