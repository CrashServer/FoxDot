(
SynthDef(\bounce,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, para1=2, para2=2.5|
	var env, snd;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	snd = CombN.ar( Decay2.ar(Impulse.ar([[para1, para2], 0.5])) * Blip.ar(freq, rate + 4), 0.2, 0.2, 0.5);

		env = EnvGen.ar(Env.adsr(atk,decay,sus,rel,peak), gate:1, doneAction:0);
	snd = Mix(snd*env);
	snd = Splay.ar(snd, level:1,spread:wide, center:pan, levelComp: true);
	snd = ReplaceOut.ar(bus, snd * amp);
}).add;
)
