SynthDef.new(\breakcore,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, buf=0, pos=0, room=0.1, sample=0, core=1, brk=12|
var osc, env, target, playbuf= PlayBuf.ar(2,buf, loop:1, rate: rate);
sus = sus * blur;
rate = In.kr(bus, 1);
target = Array.fill([4,4,8,4,8,4,4,8,8].size, buf);
osc = Breakcore.ar(buf, playbuf,  Impulse.kr(LFNoise0.ar(4, 10, brk)), LFNoise0.kr(8, 19000*core, 2000),0);
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
