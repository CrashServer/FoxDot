
(
SynthDef(\bounce, {
	arg para1=2, bus=0, para2=2.5, gate=1, amp=1, pan=0, freq=440, sus=1, blur=1, fmod=0;
	var env, snd;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	snd = CombN.ar( Decay2.ar(Impulse.ar([[para1, para2], 0.5])) * Blip.ar(freq, 4));
	
	env = EnvGen.ar(Env.adsr(), gate=1, doneAction:0);
	snd = Mix(snd) * 0.25;
	snd = Pan2.ar(snd, pan);
	snd = ReplaceOut.ar(bus, snd * amp);


}).add;
)