SynthDef.new(\formantFilter,
{|bus, formant, formantmix|
var osc;
osc = In.ar(bus, 2);
formant = (formant % 8) + 1;
osc = LinXFade2.ar(Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh, osc, 1-formantmix);
ReplaceOut.ar(bus, osc)}).add;