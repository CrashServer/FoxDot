SynthDef("subbass",
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.01, rel=0.01, blend = 250|

	var env, in, ina, synca, octa, inb, syncb, octb, octave, snd;
	sus = sus*blur;
	freq = In.kr(bus, 1);
	freq = freq/4;
	freq = [freq, freq+fmod];

	env = Env.perc(atk, sus*2, amp, [8, -1 * 8]).kr(doneAction: 0);

	/*  Input wave +/- 90 degrees - To use SinOsc.ar, replace:
	        -"iphase:  0" with "phase: pi/2"
	        -"iphase:  1" with "phase: 0"
	        -"iphase: -1" with "phase: pi"   */
	in = LFPar.ar(freq: freq * 2, iphase: 0);
	ina = LFPar.ar(freq: freq * 2, iphase: 1);
	inb = LFPar.ar(freq: freq * 2, iphase: -1);

	//Two square waves exactly out of phase and an octave below the input wave
	synca = LFPulse.ar(freq: freq, iphase: 0);
	syncb = LFPulse.ar(freq: freq, iphase: 0.5);

	//This smoothly swaps between outputting the +90 degree wave and -90 degree wave
	octa = ina * synca;
	octb = inb * syncb;
	octave = Mix.ar([octa, octb]);

	//Mixer stage, volume adjustments, envelope, and output
	snd = Mix.ar([octave * blend, in * (blend - 1)]);
    snd = LeakDC.ar(snd);
	snd = Limiter.ar(in: snd, level: 1);
	snd = snd * env;
	snd = Pan2.ar(snd,pan);

	ReplaceOut.ar(bus, snd);
},
metadata: (
		credit: "Eric Sluyter, CrashServer",
	category: \bass,
	tags: [\pitched, \bass]
	)
).add;