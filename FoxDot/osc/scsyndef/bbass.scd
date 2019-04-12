SynthDef(\bbass, { arg bus=0, freq = 440, amp = 0.5, gate = 1, pan=0, sus=1, blur=1, fmod=0;
	var snd, env, oscfreq, output, osc, envout;
	var lfo;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	oscfreq = {freq * LFNoise2.kr(Rand(0.0001,0.5)).range(0.98, 1.02)}!5;
	lfo = { SinOsc.kr({ 1/Rand(2,52) }!5) };
	env = Env.adsr(0.07, 1, 0.9, 0.1).kr(doneAction:2, gate: gate);
	output = LFSaw.ar(oscfreq, mul: lfo.value.range(0,1));
	output = RLPF.ar(output, (env*freq) + 1*freq * lfo.value.range(10/freq,5/freq), lfo.value.range(0.1,1));
	output = Splay.ar(output, lfo.value.range(0,1));
	envout=EnvGen.ar(Env.perc(level: amp,releaseTime: sus,attackTime: 0.02,curve: 'lin'), doneAction: 0);
	osc=output;
	osc = Mix(osc) * 0.1; // correct amplitude
	osc = Pan2.ar(osc * env , pan);
	ReplaceOut.ar(bus, osc * amp);
	}).add;
