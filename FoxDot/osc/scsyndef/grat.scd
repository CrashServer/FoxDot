SynthDef.new(\grat,
	{|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, bus=0, blur=1, gate=1, rate=1|
var osc, env, minfreqs, freqs, dry, osc2, osc3;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];

freqs = (freq +[0,7,12,15,19,24].midicps) /4;

minfreqs = freqs*0.5;
freqs = freqs*MouseButton.kr(1,0.75,4);
		
env=EnvGen.ar(Env(times: [(sus / 2), (sus / 2)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);

osc = LocalIn.ar(2) +  WhiteNoise.ar(0.001!2);
osc = DelayN.ar(osc,1/10-ControlDur.ir,1/20-ControlDur.ir);
osc = CombN.ar(osc!6,1/minfreqs,1/freqs,8).mean;
osc = LPF.ar(osc,8000);
		osc = HPF.ar(osc*MouseY.kr(0,5) + WhiteNoise.ar(2),80);		
		osc = RLPFD.ar(osc,MouseX.kr(200,10000,1) + WhiteNoise.kr(mul:4)*[1,1.1],0.1,0.5);
osc = osc + osc.mean;		
osc2 = LocalOut.ar(osc);
dry = osc;
10.do {
d = 0.2.rand;
osc3 = AllpassN.ar(osc,d,d,5);
};
osc = (dry + osc) * 0.125;
		osc = osc * 1/8;
osc = Pan2.ar(osc * amp, pan);
ReplaceOut.ar(bus, osc)}).add;
