SynthDef.new(\overdriveDistortion,
{|bus, drive, drivemix|
var osc;
osc = In.ar(bus, 2);
osc = LinXFade2.ar((osc * (drive * 50)).clip(0,0.2).fold2(2), osc, 1-drivemix);
ReplaceOut.ar(bus, osc)}).add;