
FoxDot Crash Server Edition - Live Coding with Python v0.7.19
=====================================

CRASH SERVER EDITS
=====================================

05/02/2019 Snd Rearange & add
### Change the default snd directory to crashSnd_mod for test ####
### Nice sounds, try : 
```python
d1 >> play("K", sample=PStep(8,1), room=PStep(18,1,0), mix=0.2, dur=1, drive=(0,0.5), octafuz=12, octamix=0.5).every(8, "stutter", Cycle([2,3,12]))
d2 >> play("-:", sample=7, mpf=5200, cut=0.9, amp=2, pan=(-1,1))
d3 >> play("x:C=", sample=var([0,5],[12,4]), rate=1, drive=1, octafuz=12)
```

31/01/2019 FX tweaking
### Tweak LPF : adds env control on lpf with lpfslide (duration) & lpfend (end filter frequency)
```python
```p2 >> noise(lpf=40, sus=4, dur=4, lpfslide=1, lpfend=800)
```

### Tweak octafuz 
### add first version of chorus with mix support 

23/01/2019 Synth Tweaking
### tweak Faim, add ADSR enveloppe: reduce CPU, Lowshelf: less boomy
```python
f1 >> faim(var([0,1,[3,-3]],[8,6,2]), dur=PDur(8,8), oct=(PStep(16,6,3),P[2:6]), lpf=2900, drive=0.7)
```
### Add Varicelle synth in experimental
### Add Square Synth, like a pulse but with phase
### Add Supersaw Synth with phase
### Add Phase to [dirt, square, supersaw, dbass]


18.12.2018
### added Legato and Disto:
```python
a1 >> blip([0,4,-2,2], dur=1/2, leg=[0,2], disto=1, smooth=0.8, distomix=0.5)
```



16.12.2018
### Mod the Chop FX
with chopwave you can choose different wave: [0:Pulse, 1:Tri, 2:Saw, 3:Sine, 4:Parabol]
with chopi=[0..1] you adjust the phase
```python
a3 >> pasha(dur=2, sus=4, chop=4, chopwave=PRand(5), chopi=PWhite(0,1), chopmix=0.7) + (0,2,4)
```


11.12.2018
### Add Faim (good bass), Prof(Prophet like), Pianovel(piano with velocity) SynthDefs
```python
f1 >> faim(dur=1/2, oct=3, sus=f1.dur*0.5, vibr=[0,3])
p1 >> prof(dur=1/2, oct=(5,6), lforate=[2,4,8], lfowidth=PWhite(0.1,1), cutoff=3500, rq=0.4)
i1 >> pianovel(PRand(8), dur=1/2, velocity=PRand(80,127), hard=[0.4,0.7], velhard=[0.2,3])
```


04.12.2018
### Update Samples

02.12.2018
### Add Flanger & Octafuz FX
```python
a1 >> blip(dur=1, flanger=linvar([0,15],24), fdecay=14, flangermix=0.5).spread()
a2 >> blip(dur=1/2, octafuz=0.2, octamix=0.7)
```

01.12.2018
### Add Jpverb FX
!!! High CPU, need more tweak, jpverb=reverb time(0.1..60), damp=damping HF (0..5)
```python
a1 >> blip(PRand(8), dur=2, jpverb=4, damp=0.19, jpverbmix=0.75)
```

29.11.2018
### added basic fx mix (Dry/Wet) controls, examples :
```python
b1 >> play("X ", drive=1, drivemix=0.5)
b2 >> play("X ", shape=2, shapemix=0.5)
b4 >> klank(sus=4, dur=4, chop=4, chopmix=1)
b5 >> klank(sus=4, dur=4, tremolo=32, tremolomix=1)
b6 >> klank(sus=4, oct=(3, 4), echo=0.5, echomix=0)
```




## Thanks

- The SuperCollider development community and, of course, James McCartney, its original developer
- PyOSC, Artem Baguinski et al
- Members of the Live Coding community who have contributed to the project in one way or another including, but not limited to, Alex McLean, Sean Cotterill, and Dan Hett.
- Big thanks to those who have used, tested, and submitted bugs, which have all helped improve FoxDot
- Thank you to those who have found solutions for SuperCollider related issues, such as DavidS48

### Samples

FoxDot's audio files have been obtained from a number of sources but I've lost record of which files are attributed to which original author. Here's a list of thanks for the unknowing creators of FoxDot's sample archive.

- [Legowelt Sample Kits](https://awolfe.home.xs4all.nl/samples.html)
- [Game Boy Drum Kit](http://bedroomproducersblog.com/2015/04/08/game-boy-drum-kit/)
- A number of sounds courtesy of Mike Hodnick's live coded album, [Expedition](https://github.com/kindohm/expedition)
- Many samples have been obtained from http://freesound.org and have been placed in the public domain via the Creative Commons 0 License: http://creativecommons.org/publicdomain/zero/1.0/ - thank you to the original creators
- Other samples have come from the [Dirt Sample Engine](https://github.com/tidalcycles/Dirt-Samples/tree/c2db9a0dc4ffb911febc613cdb9726cae5175223) which is part of the TidalCycles live coding language created by Yaxu - another huge amount of thanks.

If you feel I've used a sample where I shouldn't have, please get it touch!
