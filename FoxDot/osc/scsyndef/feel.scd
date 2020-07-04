SynthDef.new(\feel,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.1, decay=1, rel=0.01, peak=1, level=0.8, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
sus=(sus * 1.5);
amp=(amp * 0.3);
freq=(freq * [1, 1.005]);
osc=Klank.ar(`[[1, 2, 3, (3 + ((rate - 1) / 10))], [1, 1, 1, 1], [2, 2, 2, 2]], (Impulse.ar(0.0005) * Saw.ar(freq, add: 1)), freq);
osc=(osc * amp);
env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
