(
SynthDef(\total,
	{|bus = 0, amp = 0.5, fmod=0, sus=1, blur=1, freq = 220, atk=0.25, rel = 0.2, gate=1, pan = 0, slicer=0|

	var sig , sig1, sig2, sig3, env, osc;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
    sig1 = SinOscFB;
	sig2 = mean(FreqShift.ar(c=sig1.ar(sig1.ar(sig1.ar(freq/b=(1..8),1),fmod/b)+b*[fmod, 99, freq],1),1/b)+c);
	sig = sig2 ;
	sig = sig * LinSelectX.kr(slicer,[1, SinOsc.ar(4, 0, 1)]);
	env=EnvGen.ar(Env(times: [atk, (sus * 1)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
	osc = sig;
	osc=(osc * env);
osc = Mix(osc) * 0.25;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
)