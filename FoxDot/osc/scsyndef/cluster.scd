//  based on a tweet I can't find anymore :(
SynthDef(\cluster,
	{|para1=4, bus=0, mult=4, gate=1, amp=1, pan=0, freq=440, sus=1, blur=1, fmod=0|
	var env, snd;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	env = EnvGen.ar(Env.adsr(), gate=1, doneAction:2);
	snd = Splay.ar(


		LeakDC.ar(
			CombN.ar(
				SinOsc.ar(1/para1,
					Spring.ar(
						LFPulse.ar(3/4),
						4/para1,[[0.5e-1, 1.4e-3]]) *
						LFTri.ar(freq, 0, 2pi, mult * pi),
						mul: 0.5), 4, 1/4, 2))).tanh;

	snd = Mix(snd) * 0.25;
	snd = Pan2.ar(snd, pan);
	snd = ReplaceOut.ar(bus, snd * amp);


}).add;
