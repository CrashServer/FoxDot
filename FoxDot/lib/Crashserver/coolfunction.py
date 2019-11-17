############### Cool function #####################################
import os
import sys
from ..SCLang.SynthDef import SynthDefs
from ..Settings import FOXDOT_SND, FOXDOT_LOOP

try:
    import librosa
except:
    print("Error importing Sample_bpm, install librosa")

### List of synth 
synthlist = [i for i in SynthDefs][4:]
## sy >> blip().changeSynth(synthlist)

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


def find_scale(notes):
    """print all scales which contain the notes"""
    for name, scale in Scale.library().items():
            try:		
                result =  all(elem in scale for elem in notes)
            except:
                pass
            if result:
                print(name)


def binary(number):
    # return a list converted to binary from a number 
    binlist = [int(i) for i in str(bin(number)[2:])]
    return binlist


def sample_bpm(path):
    pth = os.path.join(FOXDOT_LOOP, path)
    y, sr = librosa.load(pth)
    print("BPM = ", librosa.beat.beat_track(y)[0])
    return librosa.beat.beat_track(y)[0]    


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
