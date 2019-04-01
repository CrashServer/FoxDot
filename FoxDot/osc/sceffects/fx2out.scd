SynthDef.new(\fx2out,
{|bus, fx2, tmp2, fx2_lvl|
var osc;
osc = In.ar(bus, 2);
Out.ar(3, Mix.ar(osc*fx2_lvl));
tmp2 = AudioIn.ar(2);
osc = SelectX.ar(fx2, [osc, tmp2]);
ReplaceOut.ar(bus, osc)}).add;