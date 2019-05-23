(
// an insert FX with two plugins hardcoded in series:
SynthDef.new(\insert, {arg bus, bypass1=0, bypass2=0;
    var sig = In.ar(bus, 2);
    sig = VSTPlugin.ar(sig, 2, bypass1, id: \comp);
    sig = VSTPlugin.ar(sig, 2, bypass2, id: \reverb);
	ReplaceOut.ar(bus, sig);
}).add;
)

// Search system for vsts
VSTPlugin.search(s, dir: ["C:/Program Files (x86)/VSTplugins"], useDefault: false);
VSTPlugin.pluginKeys(s)[5];

(
// insert into the FX bus
~synth = Synth(\insert, [\bus, ~fxBus], ~test, addAction: \addAfter);
// get handles to the individual VST plugins:
~fx1 = VSTPluginController(~synth, \comp);
~fx2 = VSTPluginController(~synth, \reverb);
)

~fx1.open("TDR Kotelnikov", editor: true);
~fx1.editor(show: true);

~fx2.open("ValhallaVintageVerb", editor: true);
~fx2.set(0, 0.5);
~fx2.editor(show: true);

//mix


~fx2.get(0, {arg f; f.postln;});

//Bypass
(
~synth.set(\bypass1, 1);
~synth.set(\bypass2, 1);
)

~fx2.synth.free;