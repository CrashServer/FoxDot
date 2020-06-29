SynthDef.new(\dustV,
	{|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0|
		var osc, env;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod];
		osc = GVerb.ar(CombC.ar(Dust.ar(rate+5)/Blip.ar(200,Line.kr(5,50,200),0.1),Dust.ar(1),0.01,0.02),9,9,mul:0.0001);
		env=EnvGen.ar(Env.new([1, 1], [1, 1]), doneAction:1);
		osc=(osc * env);
		osc = Mix(osc) * 1;
		osc = Pan2.ar(osc * amp, pan);
		
		ReplaceOut.ar(bus, osc)}
	).add;
