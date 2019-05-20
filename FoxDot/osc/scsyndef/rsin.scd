SynthDef(\rsin, {
	arg amp=1, gate=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8;
	var sig1, env, sig,sig2;

	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

    sig1 = VarSaw;

	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
	sig = FreeVerb2.ar(*XFade2.ar(
				SinOscFB.ar([60,4],sig1.kr(rate)+1/2),
	   			 SinOscFB.ar([freq*2,freq],526/2),sig1.kr(0.1)));
	sig = sig  * env * 0.4;
	sig = Mix(sig) * 1;
	sig = BLowShelf.ar(sig,40,1.0,-12);
	sig = LeakDC.ar(Limiter.ar(sig, 1));
	sig = Pan2.ar(sig, pan).tanh;
	ReplaceOut.ar(bus, (sig * amp));
}).add;