############### Cool function #####################################
import os
import sys
from ..SCLang.SynthDef import SynthDefs
from ..Settings import FOXDOT_SND, FOXDOT_LOOP

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