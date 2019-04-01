#####  CRASH SERVER CUSTOM STARTUP ###########
from __future__ import absolute_import, division, print_function

import os
import sys
from random import randint

### SYNTHDEFS #####
from .Crashserver.crashSynthDefs import * ### Crash Custom SynthDefs
from .Crashserver.crashFX import * ### Crash Custom Fx

### EXTENSIONS #######
from .Crashserver.speech.voice import *   ### Text2Speech
# from .Extensions.timer.hack import * ### Crash Server Timer
#from .Extensions.Video.video2 import *    ### Video player

## Path Snd
FOXDOT_SND   = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_snd/")
FOXDOT_LOOP  = os.path.realpath(FOXDOT_ROOT + "/lib/Crashserver/crash_snd/_loop_/")
FoxDotCode.use_sample_directory(FOXDOT_SND)

# OSC VIDEO FORWARD
# my_client = OSCClient()
# my_client.connect(("127.0.0.1", 12345)) # Video OSC Ip:port
# DefaultServer.forward = my_client


#########################
### CRASH SERVER SET  ###
#########################

### Longueur mesure d'intro
tmps = 4
### Language
lang = "fr"
### BPM intro
bpm_intro = 95
### Scale intro
scale_intro = "minor"
### Root intro
root_intro = "E"


##### PART I : INTRODUCTION ################

def initial():
    voix = Voix(lang=lang, rate=0.45, amp=1.0)
    voix.initi()
    #def voix1():
      #voix.intro()

    Clock.future(tmps, lambda: voix.intro())


def intro():
    Clock.bpm = bpm_intro
    Scale.default = scale_intro
    Root.default = root_intro

    def samples_crash():
      z1 >> play("z...", mpf=expvar([10,4800],[tmps,inf], start=now), amp=0.7)
      i2 >> play("I.....", amp=linvar([0,0.7],[tmps*2,inf], start=now), dur=4, rate=-0.5)


    r1 >> sos(dur=8, mpf=linvar([60,3800],[tmps*1.5, inf], start=now))
    Clock.future(tmps/2, lambda: samples_crash())
    Clock.future(tmps*1.5, lambda: initial())




















##### SDur by Quantuum #####
def SDur(target):
  sr = random.SystemRandom()
  indexes = random.randint(1,target+4)
  dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
  list=[]
  for i in range(0,indexes):
      if target%2 == 0:
          a = random.randint(1,target/2)/sr.choice(dividers)
      else:
          a = random.randint(1,(target-1)/2)/sr.choice(dividers)
      if sum(list)+a < target/2:
          list.append(a)
      if sum(list)+a < target:
          list.append(a)
  list.append(target-sum(list))
  return P[list].shuffle() # always return a list of durations with total duration equals target

# variation giving shorter durations
def SmDur(target):
  sr = random.SystemRandom()
  indexes = random.randint(1,target+4)
  dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
  list=[]
  for i in range(0,indexes):
      if target%2 == 0:
          a = random.randint(1,target/2)/sr.choice(dividers)
      else:
          a = random.randint(1,(target-1)/2)/sr.choice(dividers)
      if sum(list)+a < target/2:
          list.append(a)
      if sum(list)+a/2 < target:
          list.append(a/2)
  list.append(target-sum(list))
  return P[list].shuffle() # always return a list of durations with total duration equals target

# a variation with score-like durations
def ScDur(target):
  sr = random.SystemRandom()
  indexes = random.randint(1,target+4)
  standards = [0.25,0.375,0.75,0.5,1,2,3,4] # standard dur values found in scores
  dividers = [1,1,2] # skip 1/4 and 1/8 (comes after)
  list=[]
  for i in range(0,indexes):
      if target%2 == 0:
          a = random.randint(1,target/2)/sr.choice(dividers)
      else:
          a = random.randint(1,(target-1)/2)/sr.choice(dividers)
      if sum(list)+a < target/4:
          list.append(a)
      if sum(list)+a/2 < target/2:
          list.append(a/2)
      if sum(list)+a < target:
          list.append(a)
      if sum(list)+a/4 < target:
          list.append(a/4)
  if sum(list) < target:
      for i in range(0,len(standards)):
          if target-sum(list)%standards[i] != 0 and standards[i] < target-sum(list):
              list.append(standards[i])
      if sum(list) < target:
          list.append(target-sum(list))
  return P[list].shuffle() # always return a list of durations with total duration equals target
