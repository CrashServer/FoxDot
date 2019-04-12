SynthDef.new(\lowPassFilter,
{|bus, lpf, lpr, lpfslide, lpfend|
var osc,lpfenv;
osc = In.ar(bus, 2);
lpfenv = EnvGen.ar(Env.new([lpf, lpfend], [lpfslide]));
osc = RLPF.ar(osc, lpfenv, lpr);
ReplaceOut.ar(bus, osc)}).add;