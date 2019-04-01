SynthDef.new(\fxout,
{|bus, fx1, tmp1, fx1_lvl|
var osc;
osc = In.ar(bus, 2);
Out.ar(2, Mix.ar(osc*fx1_lvl));
tmp1 = AudioIn.ar(1);
osc = SelectX.ar(fx1, [osc, tmp1]);
ReplaceOut.ar(bus, osc)}).add;