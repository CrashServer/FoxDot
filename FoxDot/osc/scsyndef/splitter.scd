SynthDef.new(\splitter,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, buf=0, pos=0, room=0.1, sample=0, rd=0, beat_stretch=0|
var osc, env, target, playbuf= PlayBuf.ar(2,buf, loop:1, rate: rate), osc1, osc2, osc3, osc4;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / ((beat_stretch<=0) + abs(beat_stretch))) * (beat_stretch>0));
osc1 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);
osc2 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.25+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);
osc3 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.5+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);
osc4 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.75+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);
osc = Mix(osc1+osc2+osc3+osc4);
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
