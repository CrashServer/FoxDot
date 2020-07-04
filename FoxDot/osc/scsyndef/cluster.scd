//  based on a tweet I can't find anymore :(
SynthDef(\cluster,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=4.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, para1=4|
	var env, snd;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	env = EnvGen.ar(Env.adsr(atk, decay, sus, rel, peak), gate:1, doneAction:2);
	snd = Splay.ar(


		LeakDC.ar(
			CombN.ar(
				SinOsc.ar(1/para1,
					Spring.ar(
						LFPulse.ar(3/4),
						4/para1,[[0.5e-1, 1.4e-3]]) *
						LFTri.ar(freq, 0, 2pi, rate+0.01 * pi),
						mul: 0.5), 4, 1/4, 2))).tanh;

	snd = Mix(snd) * 0.4;
	snd = Pan2.ar(snd, pan);
	snd = ReplaceOut.ar(bus, snd * amp);


}).add;
