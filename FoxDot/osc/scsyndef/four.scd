(
SynthDef.new(\four,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0|
		var osc, env;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod];

		osc = SinOsc.ar([1,2,4,8],mul:0.5) * LFSaw.ar([freq,freq*1.02,freq*(fmod + 0.99),freq*1.01]);
		osc = OnePole.ar(osc, SinOsc.ar(0.1).range(-0.9,0.9));
		osc = LPF.ar(osc,SinOsc.kr(rate).range(110,8100));
		osc = AllpassN.ar(osc,0.133, 0.133, 1);
		osc = FreeVerb.ar(osc, 0.133, 1);

		env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01,sus,sus]), doneAction: 0);
		osc=(osc * env);

		osc = Mix(osc * amp) * 0.5;
		osc = Splay.ar(osc, 1, 1, pan);
		ReplaceOut.ar(bus, osc)}).add;
)