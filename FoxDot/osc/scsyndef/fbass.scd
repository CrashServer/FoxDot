SynthDef("fbass",
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=1, rel=0.2, cutoff = 250, rq = 0.35|

	var total, exciter, snd, env, sub;
	sus = sus*blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	freq = freq /4;
	total = (atk + sus + decay + rel) * freq;
	exciter = Env.new(
		levels: [0, 1, 1, 0, 0],
		times: [atk, decay, sus, rel]/total).ar;
	env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.002, 0.01, sus, sus]), doneAction: 2);
	// Delay line
	snd = CombN.ar(
		in: exciter,
		maxdelaytime: 0.06,
		delaytime: 1/freq,
		decaytime: sus);
	// LPF
	snd = RLPF.ar(
		in: snd,
		freq: LinExp.ar(Amplitude.ar(in: snd), 0, 1, cutoff, 18000),
		rq: rq);

	// Compressor for fun
	snd = CompanderD.ar(
		in: snd,
		thresh: 0.4,
		slopeBelow: 1,
		slopeAbove: 1/2.5);
	snd = Mix.ar(snd.tanh);
	snd = LeakDC.ar(snd);
	snd = snd *env* amp;
	snd = Pan2.ar(snd,pan);

    ReplaceOut.ar(bus, snd);

},
metadata: (
		credit: "Josh Mitchell, CrashServer",
	category: \bass,
	tags: [\pitched, \bass]
	)
).add;