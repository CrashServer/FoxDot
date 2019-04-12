(
SynthDef(\server_sound_close_and_personal, {
	arg amp=1, gate=1, rel=1,dur=8, bus=0, freq=200, freqs=240,pan=0, fmod=0, sus=1, vib=0;

    var sig1, env, sig,sig2;

    sig1 = VarSaw;

	freqs = (Rand(60, 40)).midicps + SinOsc.ar(Rand(0, 8));

    env = EnvGen.ar(Env(curve: 'lin',levels: [0, amp, 0],times: (sus * 1.2)), doneAction: 0);

	sig = FreeVerb2.ar(*XFade2.ar(
		SinOscFB.ar([Rand(1, 240),Rand(1, 240)],sig1.kr(Rand(1, 400))),
		  SinOscFB.ar([freqs * 1.2,freqs],sig1.kr(vib+1)+Rand(2, 2000)/2),sig1.kr(0.1)));

	sig2 = SinOscFB;
	sig2 = RLPF.ar(BrownNoise.ar(1), Rand(200, 1600), 0.015,1) * 1;

	sig = (sig + (sig2 * Rand(0, 0.01)))  * env;

	// sig = Mix(sig) * 1;

	// sig = LPF.ar(sig, 5000);
	sig = BLowShelf.ar(sig, 60);
	sig = sig * 0.5;

	sig = Pan2.ar(sig, pan).tanh;
	ReplaceOut.ar(bus, (sig * amp));


}).add;
)