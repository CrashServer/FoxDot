SynthDef.new(\feeddelay,
{|bus, feed, feedtime|
var osc,out;
osc = In.ar(bus, 2);
out = osc + Fb({		arg feedback;		osc = CombN.ar(feedback*feed + osc, 0.5, 0.25).tanh;	},0.5,0.125);
ReplaceOut.ar(bus, osc)}).add;