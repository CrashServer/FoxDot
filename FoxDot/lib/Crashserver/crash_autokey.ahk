#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetKeyDelay [0]


Numlock::
    SetCapsLockState, AlwaysOff
    SetNumLockState, AlwaysOn
  return

#Hotstring EndChars : `t

:o:.stu::.sometimes("stutter", Cycle([2])){left 12}
:o:lin::linvar([,],[,]){left 7} 
:o:var::var([,],[,]){left 7}
:o:ply::d >> play(""){left 12}
:o:.off::.sometimes("offadd", 2, 0.75){left 7}
:o:bpmvar::Clock.bpm=linvar([90,120],[64,inf],start=now){left 25}
:o:mlpf::Master().lpf=linvar([900,14000],[64,inf], start=now){left 21}
:o:crash_video::p1 >> video(vid1=5, vid1n=8.0, dur=1/2, vid1ctrl1=0, vid1ctrl2=1, vid1glitch=0, vid1hue=0.8, vid2=2, vid2n=0, vid2ctrl1=0,vid2ctrl2=0, vid2glitch=0, vid2hue=0, vidmix=0, vidblend=0, vidcode=1)
:o:reload_sample::FoxDotCode.use_sample_directory(FOXDOT_SND)


::augmentation()::
(
#########################################
# PART I : Augmentation() 
#########################################
init()

g1 >> faim([2,3,[5,7]], slide=var([0,[-4,4]], [7,1]), leg=PWhite(0,4), sus=g1.dur*PWhite(0.2,1.5), oct=4, dur=([[1,1,1/2],2,1/2,4,1/2]*PRand([2,3,1,4])), hpf=60, chop=[0,4,16], amp=0.4, room=1, mix=PWhite(0.2,0.5)).spread() + (0,[2,[4,6]])
h1 >> play("+", dur=(var([1/8,8], [16,1])), sample=2, rate=linvar([4,0.1,4], 16), amp=PWhite(0.0, 1.0), pan=PWhite(-1,1))
d1 >> play("(x.)(.x).(..x)", sample=(4,2), hpf=10, dur=var([2,1/4], 8), spf=[14000,1,30], spfslide=0.15, spfend=400)
d2 >> play("(..)(.VO).(.v.)", sample=(1,3), hpf=20, dur=4, crush=1, echo=0.5, echomix=var([0,1], [7,1]))
p1 >> play("j", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=25, dur=1/4, echotime=1, echo=1)
p2 >> play("p", sample=PRand(8), crush=4, amp=p1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
h2 >> play("[--]", sample=PRand(8), rate=var([0.7, linvar([1,4],8)]), leg=1, dur=1/4, amp=var([0,0.5], [3,4])).spread()

p3 >> play("(XP)", sample=PRand(8), rate=[0.7,1.1], leg=PRand([16,64,32]), dur=1/4, amp=var([0,p2.amp==1],[8,16]), mpf=6500)
s1 >> play("(yL) ", sample=(PRand(8), PRand(8)), dur=2, rate=(0.4, -2), delay=(0, 1), slide=(4, 1))
d3 >> play("K", dur=var([32,1/4], [1,4]), rate=linvar([2,1], 8), echo=linvar([0.125, 1], 4))

a1 >> play("I ",rate=0.25, dur=4).after(8, "stop")

a2 >> play("(Kc){.@}(0.)P", amp=1, rate=4).every(7, "stutter", Cycle([4,13,2]), hpf=4000, pan=[-1,1])
al >> play("p", rate=1, amp=bl.rate>=1, delay=0.25, sample=PRand(8))
a3 >> play("a ", sample=5, amp=1)
)

::augmentation2()::
(
### PART I.2 ####
d1 >> play("(x.).(..x.)(.x)", sample=4)
d3 >> play("(x.).(..x.)(x.)", sample=1)

d1 >> play("(x.).(..x.)((.x)(x.))", sample=[4, 4, 1, 4])
d3 >> play("(x.).(..x.)(x.)", sample=(1, 4), dur=1/4, amp=4)

b1 >> dafbass(0, dur=1/4, root=var([0, 3, 6], [4]), oct=((var([4, 5], [8]), 4.03), linvar([3, 3.03], [64])), fmod=2, dist=0.0).spread()

d4 >> play("(x.)(.x)(xo)(x.)", sample=4)
z1 >> play("z", sample=2, rate=[0.5, -0.25, -0.5], dur=8, krush=4, amp=0.5, mpf=linvar([200, 1600], [32]))
g1 >> play("@", sample=PTri(8), dur=PDur(5,8), coarse=1/8)
)

::aspiration()::
(
#################################################
# PART II : Aspiration() 
################################################# 
b1.only()

k1 >> play("(x.).(.x)(x.)", sample=(0,1,3), dur=1/2, mpf=linvar([400,8800],[240,0])).every(17, "trim", 3)
h3 >> play("[--]", amplify=k1.degree!="x", pan=[1,-1])
sn >> play("..(.u)(u.)").every(8, "bubble")
k2 >> play("<x ><  O ><->", sample=4, octer=linvar([0,1],64), dur=1/2, octersub=linvar([0, 1],[64]), octersubsub=1)
b2 >> dbass(squiz=PwRand([1, 4, 8, 16], [1, 2, 2, 4]), dur=1/4, room=1, mix=0.1)
d5 >> play("x", amp=b2.squiz>=16, squiz=4)
d6 >> play("<X:><..u.>", dur=1/4,slide=linvar([0, 4], [8, 4]),triode=PRand(128), krush=4, kutoff=4000, amplify=var([1,0],[16,16]))
)

::aspiration2()::
(
### PART II.2 ######

e1 >> play("E", sample=2, rate=linvar([0.4, 0.8], [16]), dur=var([1/4,32],[16, 1]), dist=0.1, amp=1)
b3 >> bass([0, 2, 2, 4, P[0:3], 0], dur=1/4, scale=Scale.locrian, amp=1)
d7 >> play("(x.).(..x.)(x.)", sample=(1, 4), dur=1/4, amp=4)
z2 >> play("z", sample=2, rate=[0.5, -0.25, -0.5], dur=8, krush=4, amp=0.5, mpf=linvar([200, 1600], [32]))
g1 >> play("@", sample=PTri(8), dur=PDur(5,8), coarse=1/8, bpf=0, bpr=0.1)
c1 >> creep(0, dur=1/4, oct=((3, 3.03), linvar([3, 3.03], [64])), fmod=8, hpf=linvar([400, 800], [512]), flanger=linvar([0, 1], [128]), hpr=PWhite(0.1,0.3)).spread()
)

	
::attention()::
(
#################################################
# PART III : Attention()
################################################# 

d8 >> play("X ", sample=2, mpf=4000, amp=1).every(9, "amp.offadd", -1,0.75).every(7, "stutter", 4, rate=PWhite(0.5,8), pan=[-1,1]).only()
q1 >> play("//", sample=1, dur=4, hpf=30, mpf=16000, amp=0.5, rate=4)
s2 >> play("<|a3|.><(A.).><B><b.>", dur=2, sample=2, delay=0.5, hpf=(0, 400, 100, 1000))
g1 >> play("p ", sample=2, dur=1/2, amp=0.4, leg=25, pan=PWhite(-0.25,0.25))
g2 >> play("p ", sample=1, dur=PDur([3, 5], 8), amp=0.8, leg=25, pan=PWhite(0.5,-1))
g3 >> play("q ", sample=1, dur=PDur([3, 5], 8), amp=0.8, leg=PWhite(50, 150), pan=PWhite(-0.3,0.7))
g4 >> play("q ", sample=2, dur=PDur([1, 6], 8), amp=0.8, leg=25, pan=PWhite(-1,1))
c2 >> cluster([0, 2, 0], para1=[14, 21, 28, 32, 128], mult=0, mpf=400, fmod=12, amp=1)
p4 >> prof(oct=(3,4), triode=[0,2,4,6], fmod=4, dur=1, amp=[1,0]).spread()
i2 >> play("i", dur=8, sample=6, leg=21, room=1, mix=0.2, echo=[(0.33, 0.25), 0.25],mpf=12000).spread()
)

::attention2()::
(
### PART III.2 :
s3 >> star([0, 3, [3, 7], 0.5, PRand([3, 7, 0, (0.5, 3, 0)])], crush=linvar([128, 0], [16, inf], start=now),dur=1/8, oct=6, scale=Scale.locrianMajor, formant=PRand([0, 4]), amp=0.5) + Pvar([0, 3, 0, 0, 2, 0], [4, 2])
s4 >> saw([0, 3, [3, 7], 0.5, PRand([3, 7, 0, (0.5, 3, 0)])],dur=PDur(5, 8) / 2, oct=5, octafuz=0.5, scale=Scale.minor, amp=linvar([0, 1], [128, inf], start=now), echo=0.125, echotime=s3.degree).spread() + Pvar([0, 3, 0, 0, 2, 0], [4, 2])
o1 >> play("o", dur=[8, 1/2, 1/2], sample=[3, 4, PRand(4)], delay=(0.5, [3.5, 0.5, 0.25]), echo=(1/4, 1/2), echotime=4)
t1 >> play("[tt]", dur=[8, 1/4, 4], sample=PRand(4), delay=[0.25, 0.], echo=(1/4, 1/2), echotime=4, amp=([0.5, 0.6]))
d9 >> play("d", dur=[1/2, 7, 4], sample=PRand(8), delay=2.5, echo=(1/4, 1/2), echotime=4, rate=var([1, linvar([1, 4], [4])]))
k3 >> play("<X ><  (oO) >")
f1 >> faim(PArp([0,1,0.5],11), oct=(3, 4), dur=1/4, drive=0, lpf=200)
)

::absolution()::
(
#######################################################################
# Part V: Absolution()
#######################################################################

Clock.bpm = linvar([120,150,120,60],[PRand([4, 8, 16, 2])])

i3 >> sos(dur=8).only()
p5 >> pianovel(Pvar([Scale.major, Scale.minor, Scale.locrian]).palindrome(), flanger=PWhite(0, 0.1), oct=P[3:7], mpf=Clock.bpm * 10, octafuz=0, delay=(0, 0.5, 0.05), sus=PWhite(0.5,1.2), velocity=PWhite(40,80))
p6 >> pianovel([0, 4], drive=0.1, mpf=1200, room=1, mix=0.7)    
p7 >> pianovel(PRand([Scale.minor]), dur=1, delay=0.25, amp=0.5, amplify=var([linvar([0.5, 1], [8]), 1], [8, 4]), lpf=400, oct=[3,4]).spread()
p8 >> pianovel(PRand([Scale.minor]), dur=[2,4], lpf=1400, amp=0.0, oct=[3,4]).spread()
p9 >> pianovel(p8.degree, oct=var([3, 4, 6], [PRand([2, 3, 5]), 2]), delay=PWhite(0.1, 0.9), dur=var([1/2, 8], [2, 2]), root=var([0, 5]), mpf=2800, amp=1, drive=0.0).follow(p5)
b4 >> dbass(var([0,2,-2,-1],8), dur=1/2, mpf=120)
k4 >> play("X:", mpf=120)
)

::annihilation()::
(
#######################################################################
# Part VI : Annihilation()
#######################################################################

j1 >> play("j", sample=PRand(16), room=1, mix=0.5, amp=1, rate=(PSine(16)/100,-0.25), echo=1, echotime=4, drive=PWhite(0,0.1), chop=PWhite(0,4), dur=16, spf=1900, spfslide=4, spfend=4000).spread()
k5 >> play(PEuclid2(3,8,"X","|=2|"), sample=1,rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[24,0]), triode=PRand(16), lpr=linvar([1,0.05],[24,0])).often("stutter", Cycle([2,3,12]), amp=1, hpf=1800).sometimes("amen")
k6 >> play("X(---=)", amp=2, sample=var([1, 2], [4, 4]))
k7 >> play("<V(-[VX])V-><--(pu)->", sample=3, amp=var([0, 1], [3, 5]), hpf=45).every(7, "stutter", Cycle([2, 3, 1, 2, 3, 4]))
b5 >> dirt(dur=PDur(3,var([4,8],[4,5])), amp=1, formant=PRand(8), formantmix=0.2, slidefrom=PWhite(-0.5,0.5), lpf=linvar([900,2500],[8,0])).spread().rarely("offadd", 1, 0.75).degrade(0.2).every(8, 'stutter', Cycle([4,8,6]),dur=1)
k8 >> play("<((X )(V )V )(( c)(C ))><  |A3| ><  H @>", amplify=var([1, 0], [8, 4]), mpf=6000, crush=1, hpf=PRand([2000,1000,4000]), slide=var([0, -1], [4]), bpm=var([128, 64, 256], [3, 1, 1]), sample=((4, 2), 3)).sometimes("shuffle")
)

::annihilation2()::
(
#### PART SUP ####

w7 >> play("$[$$]$[$$$]", amp=1, dur=1/1, sample=PRand(4), triode=4, rate=(0.5,1,2)).every(3, "stutter")

w1 >> saw(dur=PDur(3, 8), oct=PStep(7, 4, 3), octafuz=100, lpf=linvar([200, 4000],32), lpfend=PRand([800])  +1, lpfslide=1, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=20000)
w2 >> saw(dur=PDur([3, 5], [8, 16, 32]), amp=1, oct=7, chop=0, coarse=4, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=17000)
w3 >> jbass(sus=[8, 6,4, 8], dur=[8, 1/4, 1/4, 1/4, 1/4, 8, 1/4, 7.75, 1/4, 1/2, 1/4, 1/2], delay=(0, 4), lpf=10, amp=1, lpfslide=(0.2, 1, 0.5), lpfend=(PWhite(200, 480), PWhite(200, 480)))
w4 >> saw(dur=PDur([3, 5], [8, 16, 32]), amp=1, oct=4, chop=128, coarse=4, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=8000)
)