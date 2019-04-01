SynthDef(\ppad, {
	arg  amp=1, freq=0, gate=1, sus=1, pan=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8;
	var sig, env;

env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);

	sig=SinOsc.ar(freq+LFNoise0.ar([400,160]).range(2,40).round(2));
	sig=sig+BPF.ar(PinkNoise.ar([0.4,0.6]),freq,0.1);
	sig=sig - sig.tanh;
	sig=sig*env*amp;
	ReplaceOut.ar(bus, sig);

}).add;