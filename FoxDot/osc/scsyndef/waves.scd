(
SynthDef(\waves,
	{| amp=0.5, pan=0, bus=0, freq=220, vib=4, gate=1, sus=1, fmod=0, blur=1|
	var env, sig, sig2, osc;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

	env=EnvGen.ar(Env(times: (sus * 2),levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
	sig =  SinOsc.ar(freq * (fmod + 1), 0, freq * (vib + 4) * LFNoise1.kr(10.reciprocal).abs);
	sig2 = SinOsc.ar((freq * fmod) + sig, 0, 0.5);
	sig = SinOscFB.ar(sig2, Gendy5.ar(0.1, 0.4, 0.1, mul:0.2)) + sig2;
	sig = DelayN.ar(sig2, 0.048, 0.048);
	sig = Mix.arFill(4, { CombN.ar(sig, 0.1, LFNoise1.ar(Rand(0, 0.1), 0.04, 0.05), 15) });
	sig = AllpassN.ar(sig, 0.050, [Rand(0, 0.05), Rand(0,0.05)], 1)!4;
	sig = FreqShift.ar(sig, (freq/2)*(-1));
	//sig = LPF.ar(sig, 4200);
	sig = HPF.ar(HPF.ar(sig, 50));
	sig = FreeVerb.ar(sig);
	sig = Limiter.ar(sig).tanh;
	sig = (sig * amp) * env;
	osc = sig;
osc = Mix(osc) * 0.25;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
)