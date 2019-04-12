FoxDot.start;

StageLimiter.activate;

// SYNTHS DEFINITIONS

(
SynthDef(\mnoise, {
	arg amp=1, bus=0,mtype=0, freq=40, gate=1, sus=1, fmod=0, blur=1, vib=0, pan=0;
	var a, osc, env;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	
	
	osc = Select.ar(mtype, [
		
	LinCongN.ar(freq, 4, 0.6, 4, vib),                            
	LatoocarfianN.ar(freq + fmod, 4, 1, xi:vib),                               
	Gendy5.ar(0.1, 4, 0.1, 0, freq, freq +  fmod, ampscale: 0.1),                
	GbmanL.ar((freq*2) + fmod, xi: vib),
	CuspN.ar(freq, 1.9, xi: vib),
	StandardN.ar(freq, 1, xi: 1, yi: 2);
		
	]);
	
	osc = osc.tanh;
	osc = Limiter.ar(osc,0.999);

	
	env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01, sus/2, sus/2]), doneAction: 0);
	osc = Mix(osc) * 0.4;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, (osc * amp) * env);
		
}).add;

SynthDef(\faim, { arg bus=0, amp=0.1, sus=0.2, gate=1, pan=0, freq=200, vib=32;
	var sig;
	var sig1, sig2, sig3, sig4, sig5, sig6, sig7, sig8;
	var env1, env2, env3, env4, env5, env6, env7, env8;
	freq = freq * ((0..1)/1 - 0.5 * 0.0007 + 1);
	env1 = EnvGen.kr(Env([0,1,0.051,0],[0.001,0.01,0.8], [4,-8]), 1);
	env2 = EnvGen.kr(Env([0,1,0.051,0],[0.005,0.5,1.5], [0,-8], releaseNode:2), 1);
	env3 = EnvGen.kr(Env([0,1,1,0],[0.01,0.01,0.2], [0,0,-4], releaseNode:2), gate);
	env4 = EnvGen.kr(Env([0,1,0],[0.002,2.8], [0,-4]), 1);
	env5 = EnvGen.kr(Env([0,1,1,0],[0.001,0.1,0.8], [4,0,-4], releaseNode:2), gate);
	env6 = EnvGen.kr(Env([0,1,0],[0.001,3.0], [0,-4]), 1);
	sig1 = SinOsc.ar(freq * 11 + 0) * env1 + (SinOsc.ar(vib) * env1);
	sig2 = SinOsc.ar(freq * 6 * ( sig1 * 2.5 + 1 )) * env2;
	sig3 = SinOsc.ar(freq * 2 * 1 + 0) * env3;
	sig4 = SinOsc.ar(freq * 1 * ( sig3 * 2.5 + 1 ) + 0) * env4;
	sig5 = SinOsc.ar(freq * 1 * ( sig2 * 2.5 + 1 ) * (sig4 * 2.5 + 1)) * env5;
	sig6 = SinOsc.ar(freq * 2) * env6;
	sig = [sig1, sig2, sig3, sig4, sig5, sig6] * DC.ar([0.0, 0.0, 0.0,  0.0, 0.5, 0.5]);
	sig = sig /2;
	sig = sig.flop.sum;
	sig = sig * EnvGen.ar(\adsr.kr( Env.adsr(0.001,0,1,0.01, 1,-1) ),gate,doneAction:2);
	sig = sig * AmpComp.kr(freq);
	sig = Limiter.ar(sig);
	sig = sig.tanh;
	sig = Pan2.ar(sig, pan + [ 0, 0, 0, 0, 0, 0], amp).sum;
	ReplaceOut.ar(bus, sig);
}).add;

SynthDef(\pianovel, { |bus=0, freq=440, fmod=0, gate=1, amp=0.5, velocity=127, hard=0.8, sus=1, blur=1, velhard=0.8, pan=0, vib=0|
	var son = MdaPiano.ar([freq + fmod], gate, release: 0.9, stereo: 0.8, sustain: sus * blur, vel: velocity, hard: hard, velhard: velhard);
	son = TwoPole.ar(son, 200,0.5, mul:0.5) + son/2;
	// son = CompanderD.ar(son, 0.5, 0.5);
	DetectSilence.ar(son, 0.01, doneAction:2);
	ReplaceOut.ar(bus, Splay.ar(son * amp, 1, 1, pan));
}).add;

SynthDef(\cluster, {
	arg value=4, bus=0, mult=4, gate=0, amp=1;
	// var env = EnvGen.ar(Env.adsr(doneAction:2));
	var snd = Splay.ar(LeakDC.ar(CombN.ar(SinOsc.ar(1/value, Spring.ar(LFPulse.ar(3/value), 4/value,
		[[0.5e-1, 1.4e-3]]) *
	LFTri.ar(0.125/value, 0, 2pi, mult * pi), mul: 0.5), 4, 1/4, 2))).tanh;
	snd = ReplaceOut.ar(bus, snd * amp);
}).add;

/////Cool with small dur, low CPU////

SynthDef("prof", {
	arg amp=0.3, pan=0, freq=0, vib=0, fmod=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.5, sus=0.9, rel=0, peak=1, level=0.8, gate = 1, lforate = 0.1, lfowidth = 0.5, cutoff = 1500, rq = 0.5;

	var lfo, pulse, filter, env;
	lfo = LFTri.kr(lforate * [1, 1.01], Rand(0, 2.0) ! 2);
	pulse = Pulse.ar(freq * [1, 1.01], lfo * lfowidth + 0.5);
	filter = RLPF.ar(pulse, cutoff, rq);
	env = EnvGen.ar(
		envelope: Env.adsr(atk, decay, sus, rel, amp),
		gate: gate,
		doneAction: 2);
	Out.ar(bus, Pan2.ar(
		in: Mix(filter*amp*0.3) * env,
		pos: pan)
	);
}).add;
)
