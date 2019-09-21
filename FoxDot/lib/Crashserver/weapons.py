#coding: utf8
#!/usr/bin/env python3
from random import choice, randint
import string
from ..SCLang.SynthDef import SynthDefs
from ..Patterns import Sequences
from .Grammar import *



virus_method = ["Injecting... ", "Loading... ", "Init: ", "Dumping: ", "Hacking: ", "Run.."]
virus_name = ["MyDoom", "Brain", "Zeus", "Sality", "Virut", "Ramnit", "Blaster", "Conficker",\
"Worm", "TDSS TDL 4"]
virus_access = ["Kernel", "MBR", "Kernel", "bsdriver.sys", "Hardware", "Security", ]
virus_protocole = ["Spambot", "PWS", "Stealer", "Proxy", "BackDoor", "KeyLogger", "InfoStealer", "Cryto",\
"Autoruns", "Rootkit", "Trojan", "Rogue", "Scareware", "Script", "D.O.S." ]
virus_status = [" | [###.......] % Completed | ###",  "- Lost: 78% - ###", " @@88@@", " /Please Wait...", " |***--------| ", " , ping=3ms", "!WARNING BUFFER(#4F,5E) - VIOLATION ACCESS"]


def define_virus():
	### Generate a random virus text
	virus = "###" + choice(virus_method) + choice(virus_name) + "." + choice(virus_access) + "." + choice(virus_protocole) + choice(virus_status)  
	return virus

### Random synth
def random_virus():
	### Generate a random synth pattern
	r_player = ''.join(choice(string.ascii_lowercase) for x in range(2))
	r_synth = choice(synthdefNames)
	r_degree = str(GENERATE_PATTERN("degree"))
	r_dur = str(GENERATE_PATTERN("dur"))
	r_fx = str(GENERATE_FX())
	random_virus = '{} >> {}({}, dur={}, {})'.format(r_player, r_synth, r_degree, r_dur, r_fx)
	return random_virus

### Random Play
def random_virus_char():
	### Generate a random play pattern
	r_player = ''.join(choice(string.ascii_lowercase) for x in range(2))
	r_synth = 'play'
	r_degree = str(GENERATE_CHAR())
	r_sample = '[{}]'.format(",".join([GENERATE_INTEGER() for i in range(randint(1,len(r_degree)))]))
	r_dur = str(GENERATE_PATTERN("dur"))
	r_rate = str(GENERATE_PATTERN("dur"))
	r_fx = str(GENERATE_FX())
	random_virus_char = '{} >> {}("{}", sample={}, dur={}, rate={}, {})'.format(r_player, r_synth, r_degree, r_sample, r_dur, r_rate, r_fx)
	return random_virus_char

def random_bpm():
	'''return a var of random bpm & random dur'''
	bpm_rand = [str(randint(38,220)) for n in range(randint(2,9))] 
	var_rand = str([randint(1,16) for n in range(randint(2,9))])
	return "Clock.bpm = var([{}],{})".format(", ".join(bpm_rand), var_rand)

#{"nom": [ascii_text, dialogue, code]}

code = {
	"connect": ["Crash Server", "Welcome CrAsh ServEr \nC0nnect_the_S&rV3r \n -- StageLimiter : Active \n -- Carla : Active \n -- Record : Active", \
			'i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3]), hpf=expvar([0,500],[tmps*6, tmps*2]))'], 
	
	"init": ['Augmentation', None , \
			'g1 >> faim([2,3,[5,7]], slide=var([0,[-4,4]], [7,1]), leg=PWhite(0,4), sus=g1.dur*PWhite(0.2,1.5), oct=4, dur=([[1,1,1/2],2,1/2,4,1/2]*PRand([2,3,1,4])), hpf=60, chop=[0,4,16], amp=0.4, room=1, mix=PWhite(0.2,0.5)).spread().sometimes("shuffle") + (0,[2,[4,6]])'],
	
	"aspiration": ["Aspiration", "Faille dans le serveur detectée, risque d'instabilité niveau 2", \
			'b1 >> faim(var([-2,0],8), dur=1/4, oct=3, krush=[3,PWhite(0,3)], kutoff=linvar([400,9900],[29,11])) + var([0,P*[1,-1,2,-2]],[7,1])\n\
b2 >> faim([3,PRand(7)], dur=PDur(9,11), oct=[[5,6],4], room=0.7, mix=0.3, krush=1.8, amp=PStrum(), kutoff=PRand(400,8400), amplify=var([[1,0,1],0],[16,8])).sometimes("stutter", drive=0.2).unison(4).penta()\n\
sw >> pasha(b2.degree + (0,var(P*[6,3,2],4),4), amplify=[1,b2.amp>0.5], dur=PDur(7,9,2,var(P*[0.25,0.5,1],[6,2,4])), leg=PWhite(0,2), glide=PWhite(0.2,2), swell=0.4, sus=sw.dur*PWhite(0.1,0.9), oct=[5,6], room=1, mix=0.3).unison(4,0.125)'],
	
	"attention" : ["Attention", "Attention, le server subit une attaque de classe 3, défense activée", \
			'd8 >> play("X ", sample=2, mpf=4000, amp=1).every(9, "amp.offadd", -1,0.75).every(7, "stutter", 4, rate=PWhite(0.5,8), pan=[-1,1]).only()\n\
q1 >> play("//", sample=1, dur=4, hpf=30, mpf=16000, amp=0.5, rate=4)\n\
s2 >> play("<|a3|.><(A.).><B><b.>", dur=2, sample=2, delay=0.5, hpf=(0, 400, 100, 1000))\n\
g3 >> play("q ", sample=1, dur=PDur([3, 5], 8), amp=0.8, leg=PWhite(50, 150), pan=PWhite(-0.3,0.7))\n\
g4 >> play("q ", sample=2, dur=PDur([1, 6], 8), amp=0.8, leg=25, pan=PWhite(-1,1))\n\
c2 >> cluster([0, 2, 0], para1=[14, 21, 28, 32, 128], mult=0, mpf=400, fmod=12, amp=1)\n\
i2 >> play("i", dur=8, sample=6, leg=21, room=1, mix=0.2, echo=[(0.33, 0.25), 0.25],mpf=12000).spread()'],
	
	"corrosion": ["corrosion", None, "s3 >> star([0, 3, [3, 7], 0.5, PRand([3, 7, 0, (0.5, 3, 0)])], crush=linvar([128, 0], [16, inf], start=now),dur=1/8, oct=6, scale=Scale.locrianMajor, formant=PRand([0, 4]), amp=0.5) + Pvar([0, 3, 0, 0, 2, 0], [4, 2])\n\
f1 >> faim(PArp([0,1,0.5],11), oct=(3, 4), dur=1/4, lpf=200)"],
	
	"absolution": ["Absolution", "Le serveur est mis en quarataine, l'attaque a échouée. Ah Ah Ah Ah!", \
'Clock.bpm = linvar([120,150,120,60],[PRand([4, 8, 16, 2])]) \n\
p5 >> pianovel(Pvar([Scale.major, Scale.minor, Scale.locrian]).palindrome(), flanger=PWhite(0, 0.1), oct=P[3:7], lpf=Clock.bpm * 10, delay=(0, 0.5, 0.05), sus=PWhite(0.5,1.2), velocity=PWhite(40,80))'],
	
	"annihilation": ["Annihilation", "les défenses sont tombées, le serveur est vulnérable", \
'j1 >> play("j", sample=PRand(16), room=1, mix=0.5, amp=1, rate=(PSine(16)/100,-0.25), echo=1, echotime=4, drive=PWhite(0,0.1), chop=PWhite(0,4), dur=16, spf=1900, spfslide=4, spfend=4000).spread()\n\
k5 >> play(PEuclid2(3,8,"X","|=2|"), sample=1,rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[24,0]), triode=PRand(16), lpr=linvar([1,0.05],[24,0])).often("stutter", Cycle([2,3,12]), amp=1, hpf=1800).sometimes("amen")\n\
k6 >> play("X(---=)", amp=2, sample=var([1, 2], [14, 2]))\n\
k7 >> play("<V(-[VX])V-><--(pu)->", sample=3, amp=var([0, 1], [3, 5]), hpf=45).every(7, "stutter", Cycle([2, 3, 1, 2, 3, 4]))'],

	"random": [None, "virus généré aléatoirement", ""],
	"42": [None, None,None],
	"43": [None, None,None],

	"desynchro": [None, "Alerte!, désynchronisation du serveur temporel", random_bpm()],

	"Sin": ["-- Sin --", None, \
't2 >> rsin(dur=8, para1=2500, chop=12, chopwave=PRand(8), chopmix=0.5, lpf=400, lpr=0.6)\n\
t3 >> rsin(oct=(2,3), dur=PTri(5), vib=PRand(8), fmod=PRand([0,128,256,512]), para1=PWhite(-1050,2500), mpf=7500, coarse=t3.dur*16)\n\
n3 >> play("x.", dur=1/2, sample=4, amp=2, amplify=1, room=linvar([0.1,1],[42,0]), mix=expvar([0,0.4],16))\n\
h4 >> play("-[--]-", amplify=1, sample=4, dur=1/2, amp=PBern(16)).spread()\n\
n4 >> play("<k ><..c.>", sample=(3,3), amp=(2.5,1), hpf=60, lpf=3600, lpr=linvar([0.5,0.1],34)).sometimes("stutter", Cycle([2,3,4]), rate=PWhite(-0.1,4), hpf=380)\n\
h5 >> play("++:++", sample=PStep(8,0,2), octafuz=P[0:16]*0.1, rate=[-1,1,0.5], hpf=160).spread()\n\
s5 >> sawbass(PSine(64)*0.5, oct=(4,5,6), dur=1, amp=0.4, sus=0.5, rq=0.7, hpf=100, cutoff=linvar([100,4800],64)).offbeat(0.25).unison(4,0.125).every(32, "oct.offadd", 1, 0.25)'],

	"nucleose": ["@ Nucleose @", None, \
'a1 >> play("<X[--]><..O.>", amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))\n\
s1 >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)\n\
b1 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)'],

	"gastro": ["Gastro", None, \
'dd >> play(P["Xx.xx.xx.xx.xx.x"], sample=(0,7,4), krush=3).sometimes("stutter")\n\
ch >> play("#", dur=8, pan=(-1,1), amp=2, rate=[1,-1])\n\
sn >> play("<--o(-[--])>", krush=3, lpf=9900, lpr=PWhite(0.2,0.8), sample=2, pan=PWhite(-1,1))\n\
tt >> play("<[tt]t.t>", sample=PRand(5), pan=PWhite(-1,1), amp=var([0,1],[13,32,48]), amplify=[2.5,PWhite(0.8,2)]).sometimes("trim",2)\n\
fi >> faim(var([-2,0],32), oct=PStep([8,4],[4,2,2],3), dur=1/4, amplify=(dd.degree=="x")*2*PBern(16)) + var([0,PRand([-1,1,0.5])],[7,1])\n\
kk >> klank(PRand(8), dur=8, rate=linvar([0,1],[128]), amplify=1).unison(3)'],

	"zika": ["Zika", None, \
'b2 >> dbass(p1.degree+PWhite(0,0.3), lpf=linvar([900,4500],24), dur=[1/2,1/4,1/2,1/4,1/2]).sometimes("dur.shuffle")\n\
p1 >> prof(PSine(64)*0.2, oct=(var([(3,4),[5,6]],[6,2])), dur=PDur([5,7],8), sus=p1.dur*0.7, cutoff=7000, lforate=var([1,2,4],8), lfowidth=linvar([0.1,1],39), pan=[-1,1], amp=1.5)\n\
n1 >> play("..I.", drive=(0,0.9), sample=1, rate=(PWhite(-1,4)), amp=PBern(16), pan=linvar([-1,1],24))\n\
d4 >> play("x(---([::]:[::::]))", amp=3, sample=([0,1,2],[1,2,4])).sometimes("stutter")\n\
d6 >> play("X ", amp=2)'],

	"blank": ["__Blank", None,\
	'__null__'],
	
}

