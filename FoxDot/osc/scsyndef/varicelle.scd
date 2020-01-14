SynthDef.new(\varicelle,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, cutoff=5300, rel=0.01, peak=1, level=0.8|
var osc, oscl, oscr, sigA, sigB, sigC, env, modul;
sus = sus * blur;
freq = In.kr(bus, 1);

	modul = fmod * SinOsc.kr(rate, mul:0.5, add:0.5) * Line.kr(0, 1, 7);
		sigA = Pulse.ar(freq + modul, LFNoise2.kr(1).range(0.2, 0.8) );
		sigB = VarSaw.ar(freq + modul);
		sigC = WhiteNoise.ar() * 0.125;
		sigC = LPF.ar(sigC, freq*8);
	osc = SelectX.ar(LFNoise2.kr(2).range(0, 2), [sigA, sigB, sigC]);
	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
	osc = osc * amp * env;
	osc = Mix(osc) * 0.5;
	osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
