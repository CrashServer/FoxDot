SynthDef(\click,
	{|amp = 0.25, freq = 42, bus=0, fmod=0, blur=1, sus=1, pan = 0, vib=1, rate=10|
	var sig;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	freq = [freq, freq+fmod];
		sig = BLowPass.ar(Impulse.ar(vib,0,4), freq*(rate+0.01), 0.2);
	sig = sig + LFPar.ar(
		Env.perc(0,0.1).ar.linexp(0,1,freq, freq * 2) *
		LFDNoise3.kr(4).exprange(fmod.midiratio, 0.1.midiratio),
		-1);
	sig = sig * Env([1,0], [sus], -4).kr(2);
	sig = Mix(sig) * 0.4;
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus,Splay.ar( sig * amp ))
}).add;
