SynthDef.new(\chorus,
{|bus, chorus, chorusmix, chorusrate, chorusmax, chorusmin|
var osc,lfos,voices=8;
osc = In.ar(bus, 2);
lfos = Array.fill(8, {SinOsc.ar(chorusrate * rrand(0.95, 1.05), rrand(0.0, 1.0), (chorusmax * 0.5) - chorusmin,  (chorusmax * 0.5) + chorusmin)});
voices = DelayC.ar(osc, chorusmax,lfos);
voices = Mix.ar(voices);
osc = LinXFade2.ar(voices + osc, osc, 1-chorusmix);
ReplaceOut.ar(bus, osc)}).add;