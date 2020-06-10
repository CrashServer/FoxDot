#coding: utf8
#!/usr/bin/env python3
#####  CRASH SERVER CUSTOM STARTUP ###########
import os
import sys
import pickle
import time
from .Settings import FOXDOT_ROOT
from .Buffers import alpha, nonalpha
from .Crashserver.crash_conf import *

# copy / paste code
try:
    import pyperclip as clip
    # ASCII GENERATOR
    from pyfiglet import figlet_format, FigletFont
    fig_font = FigletFont()
    fig_fonts_list = fig_font.getFonts()
    fig_skip = ['fbr12___', 'mshebrew210', 'term', 'runic', 'pyramid', 'eftifont', 'DANC4', 'dietcola']
    fig_skip += ['emboss', 'emboss2', 'future', 'letter', 'pagga',
                      'smblock', 'smbraille', 'wideterm']
    fig_skip += ['dosrebel', 'konto', 'kontoslant']
    font_list = [x for x in fig_fonts_list if x not in fig_skip]
except:
    print("Please install pyperclip & pyfiglet")

#########################
### SERVER CONFIG     ###
#########################

file = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_gui/server_data.cs")
lostfile = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_gui/lostfile.cs")
with open(file, "rb") as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    code_server = mon_depickler.load()

with open(lostfile, "rb") as lost:
    lost_depickler = pickle.Unpickler(lost)
    lost_list = lost_depickler.load()

lost_played = lost_list[:]
server_data = code_server["server_data"]
attack_data = code_server["attack_data"]

### Lieu du Server
lieu = str(server_data["lieu"])
### Longueur mesure d'intro
tmps = int(server_data["tmps"])
### Language
lang = str(server_data["lang"])
if sys.platform.startswith("win") and lang.startswith("english"):
    lang = "english"
voice = int(server_data["voice"])
### BPM intro
bpm_intro = int(server_data["bpm_intro"])
### Scale intro
scale_intro = str(server_data["scale_intro"])
### Root intro
root_intro = str(server_data["root_intro"])
### Video
video_player = int(server_data["video"])
adresse = str(server_data["adresse"])

rate_voice = 110

### Path Snd
#crash_path = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_snd/")

sample_description_path = os.path.join(crash_path, "description.cs")
if os.path.isfile(sample_description_path):
    with open(sample_description_path, "rb") as file:
        sample_description = pickle.load(file)

gamme = ["locrianMajor", "locrian", "phrygian", "minor", "dorian", "mixolydian", "major", "lydian", "lydianAug"]
crash_function = ["lost", "binary", "desynchro", "PTime", "PTimebin" "lininf", "PDrum", "darker", "lighter", \
"human", "unison", "ascii_gen", "attack", "PChords", "fourths", "thirds", "seconds", "duree", "print_synth", "print_sample", "print_fx", "PChain2"]


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
    from .Crashserver.drumspattern2 import *
    from .Chords import *
except:
    print("Error importing Extensions : ", sys.exc_info())

### Load weapons - Code generator
try:
    from .Crashserver.weapons import *
except:
    print("Error in generating weapons code")


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
    if video_player == 1:
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
        #   Voice(crash_txt, rate=rate_voice, amp=1, lang=lang, voice=voice)

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
def ascii_gen(text="", font="standard"):
    if type(font) != str:
        font = fig_fonts_list[int(font)]
    if text != None:
        clip.copy(figlet_format(text, font=font))

##############   BEGIN ##############################################

def connect(video=video):
    Master().reset()
    Clock.set_time(0)
    lost(2)
    print(attack_data["connect"][1].strip())
    if "connect" in lost_played:
        lost_played.remove("connect")
    Clock.bpm = bpm_intro
    Scale.default = scale_intro
    Root.default = root_intro
    video_line = ""
    if video_player == 1:
        OSCVideo(adresse)
        vi >> video(vid1=0, vid2=0, vid1rate=1, vid2rate=1, vid1kal=0, vid2kal=0, vid1glitch=0, vid2glitch=0, vidblend=0, vidmix=0, vid1index=0, vid2index=0)
        video_line = "vi >> video(vid1=0, vid2=0, vid1rate=1, vid2rate=1, vid1kal=0, vid2kal=0, vid1glitch=0, vid2glitch=0, vidblend=0, vidmix=0, vid1index=0, vid2index=0)"
    i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3], start=now), hpf=expvar([0,500],[tmps*6, tmps*2]), amplify=0.5)
    clip.copy(figlet_format(attack_data["connect"][0].strip()) + "\n" + attack_data["connect"][2].strip() + "\n" + video_line)


def attack(part="", active_voice=1):
    if type(part) != str:  ### so we can type attack(42) or attack(43)
        part = str(part)

    ### next part
    elif part == "":
        part = lost_played[0]

    if part in lost_played:
        lost_played.remove(part)

    blase = attack_data[part][0].strip()
    voice_txt = attack_data[part][1].strip()
    code_txt = attack_data[part][2].strip()

    ### Define prompt
    exten = ''.join(choice(string.ascii_lowercase) for x in range(3))
    prompt = "### attack@{}.{}:~$ ".format(part, exten)

    ### Init server
    if part == "init":
        if active_voice == 1:
            init_voice()
        global time_init
        time_init = time.time()
        clip.copy(figlet_format(blase) + "\n" + prompt + define_virus()+ "\n" + code_txt)

    ### Random code generator
    if part == "42" or part == "random":   ### Random Synth code
        clip.copy(prompt + define_virus()+ "\n" + random_virus())
    elif part=="43":  ### Random play code
        clip.copy(prompt + define_virus()+ "\n" + random_virus_char())

    ### Select Part and generate Ascii text
    else:
        clip.copy((figlet_format(blase) if blase != None else "") + "\n" + prompt + define_virus()+ "\n" + (code_txt if code_txt is not None else ""))

    ### Generate Voice
    if voice_txt != None:   ### Voice generator
        if voice_txt != "" and active_voice==1:
            voice_lpf(400)
            Voice(voice_txt, rate=rate_voice + randint(0,20), lang=lang, voice=randint(1,5))
            Clock.future(calc_dur_voice(voice_txt), lambda: voice_lpf(0))

################# END #################################################

### PLAYERS METHODS
import random

@player_method
def unison(self, unison=2, detune=0.125, analog=40):
    """ Like spread(), but can specify number of voices(unison)
    Sets pan to (-1,-0.5,..,0.5,1) and pshift to (-0.125,-0.0625,...,0.0625,0.125)
    If unison is odd, an unchanged voice is added in the center
    Eg : p1.unison(4, 0.5) => pshift=(-0.5,-0.25,0.25,0.5), pan=(-1.0,-0.5,0.5,1.0)
         p1.unison(5, 0.8) => pshift=(-0.8,-0.4,0,0.4,0.8), pan=(-1.0,-0.5,0,0.5,1.0)
    """
    if unison != 0:
        pan=[]
        pshift=[]
        uni = int(unison if unison%2==0 else unison-1)
        for i in range(1,int(uni/2)+1):
            pan.append(2*i/uni)
            pan.insert(0, -2*i/uni)
        for i in range(1, int(uni/2)+1):
            pshift.append(detune*(i/(uni/2))+PWhite(0,detune*(analog/100)))
            pshift.insert(0,detune*-(i/(uni/2))+PWhite(0,-1*detune*(analog/100)))
        if unison%2!=0 and unison > 1:
            pan.insert(int(len(pan)/2), 0)
            pshift.insert(int(len(pan)/2), 0)
        self.pan = tuple(pan)
        self.pshift = tuple(pshift)
    else:
        self.pan=0
        self.pshift=0
    return self

@player_method
def human(self, velocity=20, humanize=5, swing=0):
    """ Humanize the velocity, delay and add swing in % (less to more)"""
    humanize += 0.1
    if velocity!=0:
        self.delay=[0,PWhite((-1*humanize/100)*self.dur, (humanize/100)*self.dur) + (self.dur*swing/100)]
        self.amplify=[1,PWhite((100-velocity)/100,1)]
    else:
        self.delay=0
        self.amplify=1
    return self

@player_method
def fill(self, mute_player=0, on=1):
    """ add fill to a drum player
    you can mute other players with .fill(Group(p1,d2,d3))
    0 = off
    1 = dur + amplify
    2 = dur  //  amplify =1
    3 = amplify // dur=1/2
    """ 
    if on==1:
        self.dur = PwRand([1/4,1/2,3/4],[45,45,10])
        self.amplify = var([0,1],[[PRand([3,7,15]),PRand([6,2,14])],[1,2]])*[1,PWhite(0.2,1)]
        if mute_player != 0:
            mute_player.amplify = self.amplify.map({0:1, 1:0})
    elif on==2:
        self.dur = PRand([1/4,1/2,3/4])
        self.amplify=1
    elif on==3:
        self.amplify = var([0,1],[[3,6,7,2,15,2,3,14],[1,2]])*PWhite(0,1)
        self.dur = 1/2
    else:
        self.dur = 1/2
        self.amplify = 1

@player_method
class PChain2(RandomGenerator):
    """ An example of a Markov Chain generator pattern. The mapping argument
        should be a dictionary of keys whose values are a list/pattern of possible
        destinations.  """
    def __init__(self, mapping, **kwargs):
        assert isinstance(mapping, dict)
        RandomGenerator.__init__(self, **kwargs)
        self.args = (mapping)
        self.last_value = 0
        self.mapping = {}
        i = 0
        for key, value in mapping.items():
            self.mapping[key] = [asStream(value[0]), asStream(value[1])]
            if i == 0:
                self.last_value = key
                i += 1
        self.init_random(**kwargs)
    def func(self, index):
        key = list(self.mapping[self.last_value][0])
        prob = list(self.mapping[self.last_value][1])
        #print(random.choices(key, prob))
        self.last_value = random.choices(key, prob)[0]
        return self.last_value

# END OF PLAYERS METHODS

def lost(total=0):
    global lost_played
    global lost_list
    if total==0:
        print(lost_played)
    elif total==1:
        print(lost_list)
    elif total==2:
        print("Reinit lost")
        lost_played=lost_list[:]
        print(lost_played)

def binary(number):
    """return a list converted to binary from a number"""
    binlist = [int(i) for i in str(bin(number)[2:])]
    return binlist

def duree():
    global time_init
    duree = time.time()- time_init
    print("Durée de la tentative de Crash :", time.strftime('%H:%M:%S', time.gmtime(duree)))

def desynchro():
    clip.copy(random_bpm())

def PTime():
    """Generate a pattern from the local machine time"""
    return [int(t) for t in str(Clock.get_time_at_beat(int(Clock.now()))) if t != '.']

def PTimebin():
    """Generate a pattern of actual time converted to binary"""
    return binary(int(Clock.get_time_at_beat(int(Clock.now()))))

def lininf(start=0, finish=1, time=32):
    return linvar([start,finish],[time,inf], start=now)

def PDrum(style=None, pat='', listen=False, khsor='', duree=1/2, spl = 0, charPlayer="d") :
    ''' Generate a drum pattern style '''
    ppat = ""
    dplayers = {"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5,"d6":d6,"d7":d7,"d8":d8,"d9":d9,"d0":d0}
    stopList = [p for p in dplayers.keys()]
    sample = "x-u=~r+"
    if style == None:
        print(DrumsPattern2.keys())
    else:
        patlist = [key for key in DrumsPattern2[style].keys()]
        if pat == "":
            print(DrumsPattern2[style].keys())
        elif type(pat) == int:
            if pat > len(DrumsPattern2[style])-1:
                pat = 0
                print("no more patterns...")
            player_idx = 0
            ppat = ""    
            for i in DrumsPattern2[style][patlist[pat]]:
                ply, pat, rst = i.split('"')
                if khsor != '':
                    for idx, char in enumerate(sample):
                        try:
                            pat = pat.replace(char, khsor[idx])
                        except:
                            pass    
                player_idx += 1
                ppat += f'{charPlayer}{player_idx} >> play("{pat}", dur={duree}, sample={spl})'    
                ppat += "\n"
                stopList.remove(f'd{player_idx}')
                if listen:
                    dplayers[f"d{player_idx}"] >> play(pat, dur=duree, sus=duree, sample=spl)     
            clip.copy(ppat)
            if listen:
                for p in stopList:
                    dplayers[p].stop()
            else:
                print(ppat)
        else:
            for i in DrumsPattern2[style][pat]:
                ppat += i 
                ppat += "\n" 
            clip.copy(ppat)

def darker():
    ''' Change Scale to a darkest one '''
    if Scale.default.name not in gamme:
        Scale.default = "major"
    if Scale.default.name == gamme[0]:
        print("Darkest scale reach !")
    else:
        actual = Scale.default.name
        Scale.default = gamme[gamme.index(actual) - 1]

def lighter():
    ''' Change Scale to a lightest one '''
    if Scale.default.name not in gamme:
        Scale.default = "major"
    if Scale.default.name == gamme[-1]:
        print("Lightest scale reach !")
    else:
        actual = Scale.default.name
        Scale.default = gamme[gamme.index(actual) + 1]

class PChords(GeneratorPattern):
    ''' Chords generator '''
    def __init__(self, chord=None, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.list_chords = {"I": I, "II": II, "III": III, "IV": IV, "V": V, "VI": VI, "VII":VII}
        self.last_value = None
        self.chord = None
        self.list_of_choice = []
    def func(self, index, list_of_choice=[]):
        self.list_of_choice = []
        if self.chord == None:
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

def print_video():
    clip.copy("v1 >> video(vid1=0, vid2=0, vid1rate=1, vid2rate=1, vid1kal=0, vid2kal=0, vid1glitch=0, vid2glitch=0, vidblend=0, vidmix=0, vid1index=0, vid2index=0)")

def print_synth(synth=""):
    ### Show the name and the args of a custom synth
    path = os.path.realpath(FOXDOT_ROOT + "/osc/scsyndef/")
    if synth == "":
        dir_list = os.listdir(path)
        synth_list = []
        for p in dir_list:
            files,sep,ext = p.partition('.')
            synth_list.append(files)
        print(sorted(synth_list))
    else:
        path = os.path.realpath(FOXDOT_ROOT + "/osc/scsyndef/" + synth + ".scd")
        with open(str(path), "r") as synth:
            synth = synth.readlines()
        synth_txt = [line.strip() for line in synth if line != "\n"]
        txt = str(''.join(synth_txt))
        synthname = re.findall('SynthDef[.new]*[(\\\]*(.+?),',txt)
        synthargs = re.findall('\{\|(.*)\|', txt)
        print(str(synthname[0]), " : ", str(synthargs[0]))

def print_fx(fx=""):
    ### Show the name and the args of a custom synth
    path = os.path.realpath(FOXDOT_ROOT + "/osc/sceffects/")
    if fx == "":
        dir_list = os.listdir(path)
        fx_list = []
        for p in dir_list:
            files,sep,ext = p.partition('.')
            fx_list.append(files)
        print(sorted(fx_list))
    else:
        path = os.path.realpath(FOXDOT_ROOT + "/osc/sceffects/" + fx + ".scd")
        with open(str(path), "r") as fx:
            fx = fx.readlines()
        fx_txt = [line.strip() for line in fx if line != "\n"]
        txt = str(''.join(fx_txt))
        fxname = re.findall('SynthDef[.new]*[(\\\]*(.+?),',txt)
        fxargs = re.findall('\{\|(.*)\|', txt)
        print(str(fxname[0]), " : ", str(fxargs[0]))

def print_sample(sample=""):
    # print description of samples or find the corresponding letter
    if sample=="":
        print("")
        for k, v in sorted(sample_description.items(), key= lambda x: x[0].casefold()):
            print(k.ljust(2, " ") + ': ' + v.ljust(40), end="")
        print("")
    else:
        if len(sample) == 1:
            if sample.lower() in alpha or sample.upper() in alpha or sample in nonalpha:
                print(f'{sample}: {sample_description[sample]}')
        else:
            for key, value in sample_description.items():
                if sample.lower() in value.lower():
                    print(f'{key}: {value}')

def print_loops(loop=""):
    if loop=="":
        print(loops)
    else:
        listloops = sorted([fn.rsplit(".",1)[0] for fn in os.listdir(os.path.join(FOXDOT_LOOP, loop))])
        print(listloops)



from .Crashserver.chords_dict import *

@player_method
class PMarkov(RandomGenerator):
    """ An example of a Markov Chain generator pattern. The mapping argument
        should be a dictionary of keys whose values are a list/pattern of possible
        destinations.  Mod to add probability"""
    def __init__(self, init_value="", **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.init_value = init_value
        self.active_value = 0
        self.first_value = 0
        self.second_value = 0
        self.third_value = 0
        self.mapping = {}
        self.init_random(**kwargs)
        self.turn = 0
    def stream_value(self, active_dict):
        """ Return mapping dict with a list of keys and probability"""
        for key, value in active_dict.items():
            self.mapping[key] = [asStream(value[0]), asStream(value[1])]
            #self.last_value = key
    def key_prob(self, active_dict):
        """return the key and prob of previous value from active dictionnary"""
        self.stream_value(active_dict)
        key = list(self.mapping[self.active_value][0])
        prob = list(self.mapping[self.active_value][1])
        return key, prob
    def value_choice(self, active_dict):
        """ Return a key from probabilty of active dictionnary """
        key, prob = self.key_prob(active_dict)
        return random.choices(key, prob)[0]
    def func(self, index):
        if self.turn == 0:
            if self.init_value == "":
                self.init_value = random.choice(list(cho1.keys()))
            self.active_value = self.init_value
            #print("Turn : {}, chord : {}".format(self.turn, self.active_value))
            self.turn += 1
            return self.active_value
        else:
            if self.turn == 1:
                self.first_value = self.value_choice(cho1)
                self.active_value = self.first_value
                #print("Turn : {}, chord : {}".format(self.turn, self.active_value))

            elif self.turn == 2:
                self.second_value = self.value_choice(cho2[self.init_value])
                self.active_value= self.second_value
                #print("Turn : {}, chord : {}".format(self.turn, self.active_value))

            elif self.turn == 3:
                try:
                    self.third_value = self.value_choice(cho3[self.init_value][self.first_value])
                    self.active_value = self.third_value
                except:
                    list_cho = list(cho1.keys())
                    list_cho.remove(self.init_value)
                    self.third_value = random.choice(list_cho)
                    self.active_value = self.third_value
                #print("Turn : {}, chord : {}".format(self.turn, self.active_value))

            self.turn += 1
            if self.turn > 3:
                self.turn = 0
            return self.active_value

@player_method
def switch(self, other, key, bypass=1):
    """ Switch the attr of a player
        eg: b1 >> dbass(P[0:4], amp=1)
            b2 >> blip(-2, amp=1).switch(b1, "degree")"""
    if bypass != 0:
        self_temp = self.attr[key]
        other_temp = other.attr[key]
        other.attr[key] = self_temp
        self.attr[key] = other_temp
        return self

@player_method
def clone(self, player):
    """ Clone a player, eg: a2 >> saw().clone(a1)"""
    self.attr = player.attr
    return self

### Drop ###

def drop_pattern(playTime=15, dropTime=1, reset=1):
    """ Drop the amplify to 0 for random players.
        ex : drop(6,2) => amplify=0 for random playing players at the 2 last beats of 8
    """
    totalTime = playTime + dropTime
    clkPly = [p for p in Clock.playing]
    for p in clkPly:
        p.amplify=1
    if reset!=0:    
        rndPlayerIndex = random.sample(range(0,len(clkPly)), random.randint(1,len(clkPly)))
        if rndPlayerIndex:
            for i in rndPlayerIndex:   
                clkPly[i].amplify = var([1,0],[playTime, dropTime])
                #print(f"{clkPly[i].name}.amplify = var([1,0],[{playTime}, {dropTime}])")
            #print("***".center(32, "-"))    

class Drop_pattern():
    def __init__(self, high, low):
        self.loop = True
        self.high= high
        self.low = low 
    def stop(self):
        if self.loop:
            drop_pattern(reset=0)
            self.loop = False
        else:
            self.loop = True
    def start(self, high=15, low=1, reset=0):
        drop_pattern(high, low)
        if self.loop:
            nextBar(Clock.future((high+low), lambda: self.start(high, low)))

drop = Drop_pattern(15,1)                



def drop_bpm(duree=32, nbr=0, end=4):
    """ Create a drop bpm effect (var bpm),
        duree = durée totale de la partie,
        nbr = nombre de division du drop,
        end = duree du drop en partant de la fin
        pour retablir le tempo simplement drop(92)
        """
    if nbr == 0:
        Clock.bpm = duree
    else:
        init_bpm = Clock.bpm
        actual_bpm = Clock.bpm
        divi = 1
        bpm_list = []
        duree_list = []
        for i in range(nbr):
            actual_bpm /= divi
            if actual_bpm < 10:
                actual_bpm = 10
            bpm_list.append(int(actual_bpm))
            if i == 0:
                duree_list.append(duree-end)
            else:
                duree_list.append(end/(2**i))
            divi = 2
        duree_list[-1] = end-sum(duree_list[1:-1])
        Clock.bpm = var([bpm_list], [duree_list], start=Clock.mod(8))
        print('var({}, {})'.format([bpm_list], [duree_list]))


def PMorse(text, point=1/4, tiret=3/4):
    """ Convert a string to the value of point & tiret """
    MORSE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    morse = []
    for l in text.split(" "):
        for w in l:
            for i in MORSE_DICT[w.upper()]:
                if i == ".":
                    morse.append(point)
                elif i == "-":
                    morse.append(tiret)
            morse.append(rest(5*point))
    morse[-1] += rest(2*point)
    return morse


class voice_count():
    def __init__(self):
        self.loop = True
    def stop(self):
        if self.loop:
            self.loop = False
        else:
            self.loop = True
    def start(self):
        Voice(str(random.randint(0,1000)), voice=2)
        if self.loop:
            nextBar(Clock.future(8, lambda: self.start()))

voicecount = voice_count()

#### Convert sample 
def convert(note, scale=Scale.default):
    ''' Convert note to chromatic scale'''
    def create_dict_map(scale):
        scale_cpy = copy(scale)
        scale_dict = {}
        for i in range(0,50):
            scale_dict[i] = scale_cpy[i:i+1][0] + Root.default
        return scale_dict    
    create_dict_map(scale)    
    return note.submap(create_dict_map(scale))

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

def melody(scale_melody=Scale.default.name):
    melody_dict = {
        0: [[0,1,2,3,4,5,6,7,8,9,10,11], [27,0,22,0,19,1,0,12,0,6,1,13]],
        1: [[0,1,2,3,4,5,6,7,8,9,10,11], [9,0,77,0,14,0,0,0,0,0,0,0]],
        2: [[0,1,2,3,4,5,6,7,8,9,10,11], [32,0,22,0,26,6,0,8,0,2,0,3]],
        3: [[0,1,2,3,4,5,6,7,8,9,10,11], [10,0,38,16,0,29,0,7,0,0,0,0]],
        4: [[0,1,2,3,4,5,6,7,8,9,10,11], [11,0,30,0,22,16,0,19,0,2,0,0]],
        5: [[0,1,2,3,4,5,6,7,8,9,10,11], [0,0,13,0,43,17,0,18,0,6,0,1]],
        6: [[0,1,2,3,4,5,6,7,8,9,10,11], [1,0,4,0,7,1,12,67,0,8,0,0]],
        7: [[0,1,2,3,4,5,6,7,8,9,10,11], [16,0,3,0,17,22,1,30,0,10,0,1]],
        8: [[0,1,2,3,4,5,6,7,8,9,10,11], [0,0,0,0,0,27,0,55,0,18,0,0]],
        9: [[0,1,2,3,4,5,6,7,8,9,10,11], [4,0,2,0,1,5,0,60,0,19,1,8]],
        10: [[0,1,2,3,4,5,6,7,8,9,10,11], [17,0,2,1,12,2,0,22,1,18,24,2]],
        11: [[0,1,2,3,4,5,6,7,8,9,10,11], [45,0,12,0,0,1,0,7,0,26,0,9]]
        }

    scale_melody_dict = {key: melody_dict[key] for key in melody_dict.keys() if key in Scale[scale_melody]}
    for keys, values in scale_melody_dict.items():
        note, prob = values
        fnote, fprob = zip(*((key, pro) for key, pro in zip(note, prob) if key in Scale[scale_melody]))
        scale_melody_dict[keys] = [list(fnote), list(fprob)]
    return PChain2(scale_melody_dict)


chords = {
    I: [[I, II, III, IV, V, VI], [2,2,2,39,20,35]],
    II: [[I, II, III, IV, V, VI], [3,2,1,4,86,4]],
    III: [[I, II, III, IV, V, VI], [0,5,0,85,2,8]],
    IV: [[I, II, III, IV, V, VI], [20,1,1,1,76,1]],
    V: [[I, II, III, IV, V, VI], [70,1,2,13,1,14]],
    VI: [[I, II, III, IV, V, VI], [5,5,1,49,39,1]],
    }

krhytm = {
    0.25: [0.25,0.25,0.25,0.5],
    0.5:  [0.25,0.5,0.125,0.125,0.125,0.125],
    0.125: [0.375,0.125],
    0.375: [0.375,0.375,1],
    1: [0.75,0.25],
    0.75: [0.25,1,0.125,0.125]
    }

