SynthDef.new(\ews,{|amp=0.5, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=4, peak=1, level=0.8, wide=0.0, cutoff=230, detune = 0.5, gate=1|
var osc, env;
var maxNoOfTones = 15;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
sus=(sus * 1.75);
amp=(amp / 2);
osc=Mix.fill(
		maxNoOfTones,
		{
		arg index;
		var trig, pitches, dseq_index;
		trig = Impulse.kr(0) + Dust2.kr(rate+20);
		dseq_index = Drand([0, 1, 2], inf);
		pitches =
			Lag.kr(
				Select.kr(Demand.kr(trig, 0, dseq_index), freq) + TRand.kr(detune.neg, detune, trig),
				0.2 * Rand(0.8, 1.2)
			).midicps;
		SinOscFB.ar(
			pitches,
			Rand(0, 1.22),
			1 * Lag.kr(TRand.kr(0.8, 1.0, trig), 0.2 * Rand(0.8, 1.2))
		)
		*
		(if(index < 25, 1, 0));

		}
	);
osc = Mix(osc) * (1 / 25) * Line.kr(0.0, 1.0, 0.3);
		osc = AllpassN.ar(osc, 0.050, [Rand(0, 0.05), Rand(0,0.05)], 1)!3;
		osc = RLPF.ar(osc, cutoff, 2);
	
		
env=EnvGen.ar(Env(times: [(sus), (sus)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 1;
osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
