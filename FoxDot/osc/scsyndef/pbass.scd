SynthDef.new(\pbass,
	{|bus=0, amp=0.1, atk=0.001, decay=0.01, sus=1,rel=0.01, level=0.8, peak=1, gate=1, pan=0, freq=0, fmod=0, vib=0, rate=1, blur=1, beat_dur=1, vibr=0|
  var subfreq, subenv, env, pluck, tri, sin, sub, click, sig, osc;
  sus = sus*blur;
  freq = In.kr(bus, 1);
  freq = [freq, freq+fmod];
  subfreq = freq / 2;

  // Envelopes
  subenv = EnvGen.kr(Env.perc(0, 1), doneAction:0);
  env = EnvGen.kr(Env.perc(0, 0.5));

  // Component synthesis
  pluck = Pluck.ar(PinkNoise.ar, 1, 0.2, subfreq.reciprocal) * subenv * 2;
  tri = VarSaw.ar(freq) * env;
  sin = SinOsc.ar(freq) * env;
  sub = (SinOsc.ar([subfreq, subfreq - 2, subfreq + 2]).sum * subenv).tanh;
  click = RLPF.ar(Impulse.ar(0), [2000, 8000], 1).sum * 1000;

  // Initial signal
  sig = pluck + tri + sub + click;

  // Resonant LPFs
		sig = RLPF.ar(sig, XLine.ar(freq * 100, freq * 10, sus*0.8).clip(0,20000));
		sig = sig + (MoogFF.ar(sig, freq * 10, 2.5).clip(0,20000) * 0.1);

  // EQ resulting signal
  sig = BPeakEQ.ar(sig, 400, 0.5, -9);
  sig = BPeakEQ.ar(sig, 2000, 0.5, 6);
  sig = BHiShelf.ar(sig, 8000, 1, 3);
  sig = BPeakEQ.ar(sig, 200, 1, 3);

  // Apply another envelope to dampen a bit more
  sig = sig * XLine.kr(1, 0.6, 0.1);

  // Tanh distortion / limiting
		sig = (sig * (1+rate)).tanh.clip();

  // Another round of signal coloring, using another RLPF
  // and sine components
		sig = sig + RLPF.ar(sig, XLine.ar(freq * 20, freq * 10, sus).clip(0,20000)) + sin + sub;

  // Another round of tanh distortion / limiting
		sig = (sig / 2.5).tanh;

  // Another resonant LPF
  sig = MoogFF.ar(sig, 10000, 0.1, mul:amp);
		osc = Mix(sig) * 0.3;
  osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;