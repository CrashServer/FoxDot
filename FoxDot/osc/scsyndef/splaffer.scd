SynthDef.new(\splaffer,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, buf=0, pos=0, room=0.1, sample=0, beat_stretch=0|
var osc, env, target, playbuf= PlayBuf.ar(2,buf, loop:1, rate: rate), osc1, osc2, osc3, osc4, posses, pitches;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));
posses = (pos + ((0..2)/5)).wrap(0.0, 1.0);
pitches = (0.2 * 2.0.pow(posses *rate) + SinOsc.kr(fmod, mul: fmod));
osc = PlayBuf.ar(2, buf, pitches, startPos: BufSampleRate.kr(buf) * pos, loop: 1.0);
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
