SynthDef.new(\pitchshifter,
{|bus, shift|
var osc;
osc = In.ar(bus, 2);
osc = PitchShift.ar(osc, 0.1, shift, 0.02, 0.01);
ReplaceOut.ar(bus, osc)}).add;