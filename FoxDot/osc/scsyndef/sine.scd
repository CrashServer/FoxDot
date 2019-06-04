SynthDef.new(\sine,
{|rel=0.01, rate=0, vib=0, blur=1, bus=0, beat_dur=1, fmod=0, atk=0.01, level=0.8, decay=0.01, amp=1, peak=1, pan=0, sus=1, freq=0, phase=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
osc= SinOsc.ar(freq, phase);
osc = osc * EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
