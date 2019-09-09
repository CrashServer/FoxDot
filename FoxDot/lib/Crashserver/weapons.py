#coding: utf8
#!/usr/bin/env python3
from random import choice
import string
from ..SCLang.SynthDef import SynthDefs
from ..Patterns import Sequences
from .Grammar import *


virus_method = ["Injecting... ", "Loading... ", "Init: ", "Dumping: "]
virus_name = ["MyDoom", "Brain", "Zeus", "Sality", "Virut", "Ramnit", "Blaster", "Conficker",\
"Worm", "TDSS TDL 4"]
virus_access = ["Kernel", "MBR", "Kernel", "bsdriver.sys"]
virus_protocole = ["Spambot", "PWS", "Stealer", "Proxy", "BackDoor", "KeyLogger", "InfoStealer",\
"Autoruns", "Rootkit", "Trojan", "Rogue", "Scareware"]
virus_status = [" | [###.......] % Completed | ###",  "- Lost: 78% - ###", " @@88@@", " /Please Wait...", " |***--------| ", " , ping=3ms", "!WARNING BUFFER(#4F,5E) - VIOLATION ACCESS"]


def define_virus():
	virus = "###" + choice(virus_method) + choice(virus_name) + "." + choice(virus_access) + "." + choice(virus_protocole) + choice(virus_status)  
	return virus

def random_virus():
	r_player = ''.join(choice(string.ascii_lowercase) for x in range(2))
	r_synth = choice(synthdefNames)
	r_degree = str(GENERATE_PATTERN("degree"))
	r_dur = str(GENERATE_PATTERN("dur"))
	r_fx = str(GENERATE_FX())
	random_virus = '{} >> {}({}, dur={}, {})'.format(r_player, r_synth, r_degree, r_dur, r_fx)
	return random_virus

def random_virus_char():
	r_player = ''.join(choice(string.ascii_lowercase) for x in range(2))
	r_synth = 'play'
	r_degree = str(GENERATE_CHAR())
	r_sample = '[{}]'.format(",".join([GENERATE_INTEGER() for i in range(randint(1,len(r_degree)))]))
	r_dur = str(GENERATE_PATTERN("dur"))
	r_rate = str(GENERATE_PATTERN("dur"))
	r_fx = str(GENERATE_FX())
	random_virus_char = '{} >> {}("{}", sample={}, dur={}, rate={}, {})'.format(r_player, r_synth, r_degree, r_sample, r_dur, r_rate, r_fx)
	return random_virus_char

### The Code ###
### PART I : Augmentation ###
v10 = 'g1 >> faim([2,3,[5,7]], slide=var([0,[-4,4]], [7,1]), leg=PWhite(0,4), sus=g1.dur*PWhite(0.2,1.5), oct=4, dur=([[1,1,1/2],2,1/2,4,1/2]*PRand([2,3,1,4])), hpf=60, chop=[0,4,16], amp=0.4, room=1, mix=PWhite(0.2,0.5)).spread().sometimes("shuffle") + (0,[2,[4,6]])'

v11 = 'b1 >> faim(var([-2,0],8), dur=1/4, oct=3, krush=[3,PWhite(0,3)], kutoff=linvar([400,9900],[29,11])) + var([0,P*[1,-1,2,-2]],[7,1]) \n\
b2 >> faim([3,PRand(7)], dur=PDur(9,11), oct=[[5,6],4], room=0.7, mix=0.3, krush=1.8, amp=PStrum(), kutoff=PRand(400,8400), amplify=var([[1,0,1],0],[16,8])).sometimes("stutter", drive=0.2).unison(4).penta()'
part1 = [v10, v11]

# Part II : Aspiration()   #
v20 = 'sa >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)\n\
b3 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)'

v21 = 'b2 >> dbass(squiz=PwRand([1, 4, 8, 16], [1, 2, 2, 4]), dur=1/4, room=1, mix=0.1)'

v22 = 'b3 >> bass([0, 2, 2, 4, P[0:3], 0], dur=1/4, scale=Scale.locrian, amp=1)'
part2 = [v20,v21,v22]

# Part III : Attention()   #
v30 = 'd8 >> play("X ", sample=2, mpf=4000, amp=1).every(9, "amp.offadd", -1,0.75).every(7, "stutter", 4, rate=PWhite(0.5,8), pan=[-1,1]).only()\n\
q1 >> play("//", sample=1, dur=4, hpf=30, mpf=16000, amp=0.5, rate=4)\n\
s2 >> play("<|a3|.><(A.).><B><b.>", dur=2, sample=2, delay=0.5, hpf=(0, 400, 100, 1000))\n\
g1 >> play("p ", sample=2, dur=1/2, amp=0.4, leg=25, pan=PWhite(-0.25,0.25))\n\
g2 >> play("p ", sample=1, dur=PDur([3, 5], 8), amp=0.8, leg=25, pan=PWhite(0.5,-1))\n\
g3 >> play("q ", sample=1, dur=PDur([3, 5], 8), amp=0.8, leg=PWhite(50, 150), pan=PWhite(-0.3,0.7))\n\
g4 >> play("q ", sample=2, dur=PDur([1, 6], 8), amp=0.8, leg=25, pan=PWhite(-1,1))\n\
c2 >> cluster([0, 2, 0], para1=[14, 21, 28, 32, 128], mult=0, mpf=400, fmod=12, amp=1)\n\
p4 >> prof(oct=(3,4), triode=[0,2,4,6], fmod=4, dur=1, amp=[1,0]).spread()\n\
i2 >> play("i", dur=8, sample=6, leg=21, room=1, mix=0.2, echo=[(0.33, 0.25), 0.25],mpf=12000).spread()'
part3 = [v30]

code = [part1,part2,part3]