SynthDef.new(\fx2out,
{|bus, fx2|
var osc;
osc = In.ar(bus, 2);
Out.ar(3, Mix.ar(osc*fx2));
ReplaceOut.ar(bus, osc)}).add;