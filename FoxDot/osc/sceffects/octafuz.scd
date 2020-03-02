SynthDef.new(\octafuz,
{|bus, octafuz, octamix|
var osc, env, dis;
dis = [1,1.01,2,2.02,4.5,6.01,7.501];
dis = dis ++ (dis*12);
osc = In.ar(bus, 2);
osc = ((osc * dis*octafuz).sum.distort*4);
osc = (osc * 1/16)!2;
ReplaceOut.ar(bus, osc)}).add;
