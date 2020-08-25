SynthDef(\virus, {
	arg len = 2, freq = 420, fmod = 0.1, vib = 0.25, rate = 1, gate = 1, bus=0, amp=1;
	var mainEnv = EnvGen.kr(Env.triangle(len,1), gate, doneAction:2);
	var speed = Array.geom(4, rate, [1.75, 1.25].choose);
	var freqs = Array.geom(8, freq/2, 1.5);
	var pulse = {|rat1,rat2|LFPulse.ar(rat1, [0,0.5,1].choose)*LFPulse.ar(rat2)};
	var a = Lag.ar(HenonN.ar(
		speed.choose*(mainEnv*10000.rand),
		fmod, vib,
	), 0.01);
	var bass = SinOsc.ar(freqs!2*(a*1.0.rand), 0, Lag.ar(pulse.(rate, speed.choose), 0.001));
	var tone1 = SinOsc.ar([(freqs+Rand(0,5))*a,(freqs+Rand(0,5))*a], 0, 0.01*pulse.(speed.choose, speed.choose));
	var tone2 = Pan2.ar(SinOsc.ar(freqs.choose*a, 0, 0.1*pulse.(speed.choose, rate)), a);
	var tone3 = SinOsc.ar([freqs.choose,freqs.choose*a], 0, 0.05*pulse.(speed.choose, rate))*mainEnv.round(0.25);
	var noise = Pan2.ar(PinkNoise.ar(a*0.1*pulse.(rate,rate)), a);
	var impulse = RLPF.ar(Impulse.ar(pulse.(rate, speed.choose), a), freqs.choose+(a*10), 0.01, 0.1).tanh;
	var osc = (bass+tone1+tone2+tone3+noise+impulse).tanh;
	ReplaceOut.ar(bus, osc * amp);
	}
).add;
