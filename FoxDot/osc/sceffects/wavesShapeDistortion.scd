SynthDef.new(\wavesShapeDistortion,
{|bus, shape, shapemix|
var osc;
osc = In.ar(bus, 2);
osc = LinXFade2.ar((osc * (shape * 50)).fold2(1).distort / 5, osc, 1-shapemix);
ReplaceOut.ar(bus, osc)}).add;