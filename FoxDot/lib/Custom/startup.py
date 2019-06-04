# coding: utf8
#!/usr/bin/env python3
#####  CRASH SERVER CUSTOM STARTUP ###########
from __future__ import absolute_import, division, print_function

import os
import sys

### SYNTHDEFS #####
try:
	from .Crashserver.crashSynthDefs import * ### Crash Custom SynthDefs
	from .Crashserver.crashFX import * ### Crash Custom Fx
	from .Crashserver.Buffers_crash import * ### Crash Buffers
except:
	print("Error importing SynthDefs, FX or Loop player : ", sys.exc_info()[0])

### EXTENSIONS #######
try:
	from .Crashserver.speech.voice import *   ### Text2Speech
	from .Crashserver.arpy import *
	from .Crashserver.sdur import *
	from .Chords import *
	# from .Extensions.timer.hack import * ### Crash Server Timer
	#from .Extensions.Video.video2 import *    ### Video player
except:
	print("Error importing Extensions : ", sys.exc_info()[0])


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
		
	my_client = FilterOSCClient()
	my_client.connect(("192.168.0.14", 12345))
	Server.forward = my_client
except:
	print("Error forwarding OSC to video", sys.exc_info()[0])

#########################
### CRASH SERVER SET  ###
#########################

### Lieu du Server
lieu = str("de l'elastique bar")
### Longueur mesure d'intro
tmps = 16
### Language
lang = "fr"
### BPM intro
bpm_intro = 98
### Scale intro
scale_intro = "minor"
### Root intro
root_intro = "E"
### Setup
part = ["augmentation()", "aspiration()", "attack()", "attention()", "absolution()", "annihilation()"]


##############   BEGIN ##############################################

##### PART I : INTRODUCTION ################
	
try: 
	def init():
		voix = Voice(lang=lang, rate=0.45, amp=1.0)
		voix.initi(lieu)
		Clock.future(tmps, lambda: voix.intro())
except:
	print("Error in intro Inital function", sys.exc_info()[0])

try:
	def connect():
		print("Welcome CrAsh ServEr \nC0nnect_the_S&rV3r")
		Clock.bpm = bpm_intro
		Scale.default = scale_intro
		Root.default = root_intro
		
		def samples_intro():
			#z1 >> play("z...", mpf=expvar([10,4800],[tmps,inf], start=now), amp=0.7)
			i1 >> play("I.....", amp=linvar([0,0.7],[tmps*2,tmps*4], start=now), dur=PRand([4,8,2,16]),rate=-0.5, room=PWhite(0,1), mix=PWhite(0,0.6))

		i3 >> sos(dur=8, mpf=linvar([60,3800],[tmps*1.5, tmps*3], start=now)).only()
		vi >> video(vid=0, speed=1, vfx1=0, vfx2=0)
		
		#Clock.future(tmps*1.5, lambda: init())
		Clock.future(tmps, lambda: samples_intro())
except:
	print("Error in connect function", sys.exc_info()[0])


################# END #################################################

def lost(partie):
	print(part[partie])

def OSCVideo(adresse):
	my_client = FilterOSCClient()
	my_client.connect((adresse, 12345))
	Server.forward = my_client

### List of synth 
synthlist = []
for i in SynthDefs:
    synthlist.append(i)

def check_available_sample(path=FOXDOT_SND):    
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            numb = len(filenames)
            if 0 < numb < 10:
                pth = dirpath.split(path)[-1]
                char, uplow = os.path.split(pth)
                if uplow == "lower":
                    descr = DESCRIPTIONS[str(char[1:]).lower()]
                elif uplow == "upper":
                    descr = DESCRIPTIONS[str(char[1:]).upper()] 
                #print(descr)
                print(dirpath.split(path)[-1], " : ", str(10-numb), "slots, ", descr)
    else:
        print("Directory {} doesn't exist".format(path))
