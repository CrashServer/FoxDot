SynthDef.new(\octafuz,
{|bus, octafuz, octamix|
var osc,osc_low,osc_filtered;
osc = In.ar(bus, 2);
osc_low = LPF.ar(osc, 200);
osc_low = osc_low * 4;
osc_low = FreqShift.ar(osc_low, [200, 60]);
osc_filtered = LPF.ar(osc, 40);
osc_filtered = LPF.ar(osc, 50);
osc_filtered = Amplitude.ar(osc_low, attackTime:0.1, releaseTime: 0.5, mul: 4.0).abs;
osc = LinXFade2.ar((Clip.ar(TwoPole.ar(osc * ((osc_filtered * octafuz) * 10), [60, 20000], 0.9), -0.75, 4).tanh + osc_low) / 4, osc, 1-octamix);
ReplaceOut.ar(bus, osc)}).add;