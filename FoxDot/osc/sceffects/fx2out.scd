SynthDef.new(\fx2out,
{|bus, fx2, lpfx2, hpfx2|
var osc,fxsig;
osc = In.ar(bus, 2);
fxsig = LPF.ar(osc, lpfx2);
fxsig = HPF.ar(fxsig, hpfx2);
Out.ar(3, Mix.ar(fxsig*fx2));
ReplaceOut.ar(bus, osc)}).add;