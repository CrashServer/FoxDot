SynthDef.new(\fxout,
{|bus, fx1|
var osc;
osc = In.ar(bus, 2);
Out.ar(2, Mix.ar(osc*fx1));
ReplaceOut.ar(bus, osc)}).add;