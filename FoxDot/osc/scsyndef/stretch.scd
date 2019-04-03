SynthDef.new(\stretch,
{|sus=1, amp=1, decay=0.01, sample=0, rel=0.01, rate=1.0,dur=4, gate=1, level=0.8, pan=0, beat_dur=1, vib=0, buf=0, peak=1, fmod=0, pos=0, atk=0.01, freq=0, bus=0, room=0.1, blur=1, loopRel=0, startPos=0, startLoop, endLoop, ipol=2|
var osc, env;
sus = sus * blur;
osc = LoopBuf.ar(1, buf, BufFrames.kr(buf) / (dur * 44100), 0, 0, 0
			, BufFrames.kr(buf), 1);
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
