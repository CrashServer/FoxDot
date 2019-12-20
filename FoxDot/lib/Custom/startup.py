#coding: utf8
#!/usr/bin/env python3
#####  CRASH SERVER CUSTOM STARTUP ###########
import os
import sys
import pickle
from .Settings import FOXDOT_ROOT
# copy / paste code
import pyperclip as clip
# ASCII GENERATOR
from pyfiglet import figlet_format


#########################
### SERVER CONFIG     ###
#########################

file = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_gui/server_data.cs")
with open(file, "rb") as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	code_server = mon_depickler.load()

server_data = code_server["server_data"]
attack_data = code_server["attack_data"]

### Lieu du Server
lieu = str(server_data["lieu"])
### Longueur mesure d'intro
tmps = int(server_data["tmps"])
### Language
lang = str(server_data["lang"])
voice = int(server_data["voice"])
### BPM intro
bpm_intro = int(server_data["bpm_intro"])
### Scale intro
scale_intro = str(server_data["scale_intro"])
### Root intro
root_intro = str(server_data["root_intro"])
### Video  
video = int(server_data["video"])
adresse = str(server_data["adresse"])

rate_voice = 100
# ### Lieu du Server
# lieu = str("de euh meille zine")
# ### Longueur mesure d'intro
# tmps = 16
# ### Language
# lang = "french"
# voice = 0
# ### BPM intro
# bpm_intro = 48
# ### Scale intro
# scale_intro = "minor"
# ### Root intro
# root_intro = "E"
# ### Video  
# video = 0
# adresse = "192.168.0.22"

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
	from .Crashserver.drumspattern import *
	from .Chords import *
	#from .Crashserver.coolfunction import *
	# from .Extensions.timer.hack import * ### Crash Server Timer
	#from .Extensions.Video.video2 import *    ### Video player
except:
	print("Error importing Extensions : ", sys.exc_info())

### Load weapons - Code generator
try:
	from .Crashserver.weapons import *
except:
	print("Error in generating weapons code")

### Path Snd
crash_path = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_snd/")

try: 
	FOXDOT_SND   = crash_path
	FOXDOT_LOOP  = os.path.realpath(crash_path + "/_loop_/")
	FoxDotCode.use_sample_directory(FOXDOT_SND)
	Samples.addPath(FOXDOT_LOOP)
	loops = sorted([fn.rsplit(".",1)[0] for fn in os.listdir(FOXDOT_LOOP)])
except:
	print("Error importing Custom Sound", sys.exc_info()[0])

### OSC VIDEO Filtered FORWARD
try:
	if video == 1:
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
		#Clock.future(tmps, lambda: voix.intro())
	elif sys.platform.startswith("linux"):
		serv = init_server(lang, lieu)
		txt_init = serv.initi()
		#crash_txt = serv.crash_txt()
		Voice(txt_init, rate=rate_voice, amp=1, lang=lang, voice=voice)
		#def txt_intro():
		#	Voice(crash_txt, rate=rate_voice, amp=1, lang=lang, voice=voice)
			
		#Clock.future(tmps, lambda: txt_intro())	
	else:
		print("Sorry, we crash only from windows or linux")

### LPF during Txt 2 Speech
def voice_lpf(freq=400):
	Master().lpf=freq

def calc_dur_voice(phrase=""):
	phrase = len(phrase.split())
	try:
		if phrase or phrase > 0:
			return (Clock.seconds_to_beats(phrase * 0.6))
		else:
			return 8
	except:
		return 8

### Generate ASCII from text into the clipboard 
def ascii_gen(text=""):
	if text is not None:
		clip.copy(figlet_format(text))

##############   BEGIN ##############################################
main_part = ["init", "connect", "aspiration", "attention", "corrosion", "absolution", "annihilation"]

def connect(video=video):
	print(attack_data["connect"][1])
	Clock.bpm = bpm_intro
	Scale.default = scale_intro
	Root.default = root_intro
	if video==1:
		OSCClient(adresse)
		vi >> video(vid=0, speed=1, vfx1=0, vfx2=0)		
	i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3], start=now), hpf=expvar([0,500],[tmps*6, tmps*2]))
	clip.copy(figlet_format(attack_data["connect"][0]) + "\n" + attack_data["connect"][2])


def attack(part="default"):
	if type(part) is not str:  ### so we can type attack(42) or attack(43)
		part = str(part)

	### Random choice of Part
	elif part == "default":    
		part = choice([i for i in code.keys() if i not in main_part])
	
	blase = attack_data[part][0].strip()
	voice_txt = attack_data[part][1].strip()
	code_txt = attack_data[part][2].strip()

	### Define prompt
	exten = ''.join(choice(string.ascii_lowercase) for x in range(3))
	prompt = "### attack@{}.{}:~$ ".format(part, exten)
	
	### Init server
	if part == "init":    
		init_voice()
		clip.copy(figlet_format(blase) + "\n" + prompt + define_virus()+ "\n" + code_txt)
	
	### Random code generator
	if part == "42" or part == "random":   ### Random Synth code
		clip.copy(prompt + define_virus()+ "\n" + random_virus())
	elif part=="43":  ### Random play code
		clip.copy(prompt + define_virus()+ "\n" + random_virus_char())
	
	### Select Part and generate Ascii text
	else:
		clip.copy((figlet_format(blase) if blase is not None else "") + "\n" + prompt + define_virus()+ "\n" + (code_txt if code_txt is not None else ""))
	
	### Generate Voice
	if voice_txt is not None:   ### Voice generator
		if voice_txt is not "":
			voice_lpf(400)
			Voice(voice_txt, rate=rate_voice, lang=lang, voice=randint(1,5))		
			Clock.future(calc_dur_voice(voice_txt), lambda: voice_lpf(0))

################# END #################################################
crash_function = ["lost", "binary", "desynchro", "PTime", "PTimebin" "lininf", "PDrum", "darker", "lighter", "human", "unison", "ascii_gen", "attack", "PCircle"]


def lost(mainpart=1):
	if mainpart==0:
		print([i for i in attack_data.keys() if int(attack_data[i][3]) > 0])
	else:
		print([i for i in attack_data.keys()])

def binary(number):
    # return a list converted to binary from a number 
    binlist = [int(i) for i in str(bin(number)[2:])]
    return binlist

def desynchro():
	clip.copy(random_bpm())    	

def PTime():
    ### Generate a pattern from the local machine time
    return [int(t) for t in str(Clock.get_time_at_beat(int(Clock.now()))) if t is not '.']

def PTimebin():
	### Generate a pattern of actual time converted to binary
	return binary(int(Clock.get_time_at_beat(int(Clock.now()))))

def lininf(start=0, finish=1, time=32):
    return linvar([start,finish],[time,inf], start=now)

def PDrum(style=None):
	# Generate a drum pattern style
	if style == None:
		print(DrumsPattern.keys())
	else:	
		clip.copy(DrumsPattern[style])

gamme = ["locrianMajor", "locrian", "phrygian", "minor", "dorian", "mixolydian", "major", "lydian", "lydianAug"]

def darker():
    ### Change Scale to a darkest one
    if Scale.default.name not in gamme:
        Scale.default = "major"
    if Scale.default.name == gamme[0]:
        print("Darkest scale reach !")
    else:
        actual = Scale.default.name        
        Scale.default = gamme[gamme.index(actual) - 1]

def lighter():
	### Change Scale to a lightest one
    if Scale.default.name not in gamme:
        Scale.default = "major"
    if Scale.default.name == gamme[-1]:
        print("Lightest scale reach !")
    else:
        actual = Scale.default.name        
        Scale.default = gamme[gamme.index(actual) + 1]

class PChords(GeneratorPattern):
    def __init__(self, chord=None, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.list_chords = {"I": I, "II": II, "III": III, "IV": IV, "V": V, "VI": VI, "VII":VII}
        self.last_value = None
        self.chord = None
        self.list_of_choice = []
    def func(self, index, list_of_choice=[]):
        self.list_of_choice = []
        if self.chord is None:
            self.chord = tuple(self.list_chords[choice(list(self.list_chords))])
        for keys, values in self.list_chords.items():
            for note in values:
                if note in list(self.chord):
                    if values not in self.list_of_choice:
                        self.list_of_choice.append(values)
        self.list_of_choice.remove(self.chord)
        self.last_value = choice(self.list_of_choice)
        self.chord = self.last_value
        return self.last_value


### Chord progression, Root mouvement by fourths, thirds, seconds
fourths = PChain({
    I: [IV, V],
    II: [V, VI],
    III: [VI, VII],
    IV: [VII, I],
    V: [I, II],
    VI: [II, III],
    VII: [III, IV]   
})

thirds = PChain({
    I: [III, VI],
    II: [IV, VII],
    III: [I, V],
    IV: [II, VI],
    V: [III, VII],
    VI: [I, IV],
    VII: [II, V]   
})

seconds = PChain({
    I: [II, VII],
    II: [I, III],
    III: [II, IV],
    IV: [III, V],
    V: [IV, VI],
    VI: [V, VII],
    VII: [VI, I]   
})