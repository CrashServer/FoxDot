(
SynthDef(\radio,
	{| bus=0, freq=800, gate=1, amp=0.5, pan=0, rel=3, rate=1|
	var env, osc, sig;
	env = EnvGen.ar(Env.asr(0,1,rel),gate,doneAction:2);
	sig = Pan2.ar(CombN.ar(Resonz.ar(Gendy5.ar(1,40,minfreq:0.2,maxfreq:freq,durscale:0.1,initCPs:10),freq * rate,0.1),0.1,5,0.6));
	sig = FreeVerb.ar(sig, 0.1, 0.5);
	osc = Mix(sig) * 0.5;
	osc = Limiter.ar(osc);
	osc = Splay.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
)