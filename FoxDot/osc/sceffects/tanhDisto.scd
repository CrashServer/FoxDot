SynthDef.new(\tanhDisto,
{|bus, tanh|
var osc;
osc = In.ar(bus, 2);
osc = (osc*tanh+3).tanh*0.4;
ReplaceOut.ar(bus, osc)}).add;