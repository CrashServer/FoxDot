(
// SynthDefs

// FreqScope.new(width: 522, height: 300, busNum: 0);
////////////////////////////////////////////////////////////////////////////////////////////
////////////// I. NOISE GENERATORS
// 1. mnoise : a chaosGen based Synth with multiple variations
// 2. glitchcore : synth with a noise background, can be chaotic
// 3. cluster : bouncing drums
// 4. rsin : noise + higher pitched sound, oscillation, versatile
// 5. Electric : dark synths with chaotic Ugens
// 6. radio : radio static / noise texture
// 7. Drone : u guessed it, some kind of drone/perturbation
// 8. Table : no description here, try it
// 9. The filler, plays fast notes but not only
// 10. Garfield, don't be scared
////////////////////////////////////////////////////////////////////////////////////////////
////////////// II. BASS SYNTHS
// 1. Faim  : the classic
// 2. Faim2 : the classic, updated
////////////////////////////////////////////////////////////////////////////////////////////
////////////// III. DRUMS or DRUM-LIKE
// 1. Click : sounds drum like but try to change fmod to high values and things get craaaazzyyy & vib
////////////////////////////////////////////////////////////////////////////////////////////
////////////// IV. PADS
// 1. Hoover
// 2. total : an evolving soundscape
// 3. SynthWave : mysterious

////////////////////////////////////////////////////////////////////////////////////////////
////////////// V. INSTRUMENTS


////////////////////////////////////////////////////////////////////////////////////////////
// I. NOISE BASED
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////

// 1. MNOISE
// ChaosGens synth, use selector (mtype), from 0 to 5 to switch UGens, the vib parameter is not really a vib but changes some stuff, can make some great basslines with some params.
// can be used as a noise gen on lower freq or bassline. Some combinations don't work well some mtype and low oct for ex, nearly always add some vib

SynthDef(\mnoise, {
	arg amp=1, bus=0,mtype=0, freq=40, gate=1, sus=1, fmod=0, blur=1, vib=0, pan=0;
	var a, osc, env;
	freq = In.kr(bus, 1);
	sus = sus * blur;


	osc = Select.ar(mtype, [

	LinCongN.ar(freq, 4, 0.6, 4, vib),
	LatoocarfianN.ar(freq + fmod, 4, 1, xi:vib),
	Gendy5.ar(0.1, 4, 0.1, 0, freq, freq +  fmod, ampscale: 0.1),
	GbmanL.ar((freq*2) + fmod, xi: vib),
	CuspN.ar(freq, 1.9, xi: vib),
	StandardN.ar(freq, 1, xi: 1, yi: 2);

	]);

	osc = osc.tanh;
	osc = Limiter.ar(osc,0.999);


	env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01, sus/2, sus/2]), doneAction: 0);
	osc = Mix(osc) * 0.4;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, (osc * amp) * env);

}).add;


// 2. GLITCHCORE
// synth with a noise background, can be chaotic but fun
// ex : p1 >> glitchcore(5, dur = 4, sawFreq=4, fmod=128, lpf=0, hpf=0)


SynthDef(\glitchcore, {
	arg bus =0, amp= 0.5, gate=1, dur=1, sawFreq=1, pan=0, freq=440, fmod=0;
	var sigbase, sigmod, sig, env, env2, bass;
	env =  EnvGen.ar(Env.adsr(0, 0, 0.5, dur), gate, doneAction: 2);
	env2 = EnvGen.ar(Env.perc(0, 0.1), gate);
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	sigbase = LocalBuf(1e4,2).clear;
	bass = CombL.ar(env2 * SinOsc.ar(freq, mul: 8), 8);
	sigmod = Sweep.ar(BufRd.ar(2, sigbase, Saw.ar(sawFreq, 4, 125)), 5e5);
	sig = BufWr.ar(SinOsc.ar([1, 120]), sigbase, sigmod);
	sig = BufRd.ar(2, sigbase, sigmod) ;
	sig = (sig.tanh + bass);
	sig = sig + RHPF.ar(sig,3200, 1, 2);
	sig = sig + 2 * BPF.ar(sig, 200, 2);
	sig  = Mix(sig) * 0.4;
	sig = Limiter.ar(sig, 0.99);
	sig = Pan2.ar(sig * amp, pan);
    ReplaceOut.ar(bus, sig * env);
}).add;

// 3. Cluster
// don't recall the source of this synth, but modified to make some kind of bouncing drums
// warning had a few crashed...gotta fix that

SynthDef(\cluster, {
	arg para1=4, bus=0, mult=4, gate=1, amp=1, pan=0, freq=440, sus=1, blur=1, fmod=0;
	var env, snd;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	env = EnvGen.ar(Env.adsr(), gate=1, doneAction:2);
	snd = Splay.ar(


		LeakDC.ar(
			CombN.ar(
				SinOsc.ar(1/para1,
					Spring.ar(
						LFPulse.ar(3/4),
						4/para1,[[0.5e-1, 1.4e-3]]) *
						LFTri.ar(freq, 0, 2pi, mult * pi),
						mul: 0.5), 4, 1/4, 2))).tanh;


	snd = Mix(snd) * 0.5;
	snd = Pan2.ar(snd, pan);
	snd = ReplaceOut.ar(bus, snd * amp);


}).add;

/// 4. RSIN
//  dark noisy background with some high pitch tones, evolves can do some perc atks
// examples :
// b1 >> rsin(oct=2, dur=2, amp=0.5, para1=500, vib=0, fmod=256)
// b1 >> rsin(oct=3, dur=2, amp=0.5, para1=5000, vib=4, fmod=512)


SynthDef(\rsin, {
	arg amp=1, gate=1, rel=1, dur=1, bus=0, freq=440, para1=2000, pan=0, fmod=0, sus=1, vib=0;
	var sig1, env, sig,sig2;

	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

    sig1 = VarSaw;
	env = EnvGen.ar(Env.adsr(0, 0, 1, dur, 1.2, curve: -3), gate, doneAction:2);
	sig = FreeVerb2.ar(*XFade2.ar(
				SinOscFB.ar([60,4],sig1.kr(para1)+1/2),
	   			 SinOscFB.ar([freq*2,freq],sig1.kr(vib+1)+526/2),sig1.kr(0.1)));
	sig = sig  * env;
	sig = Mix(sig) * 1;
	sig = LeakDC.ar(Limiter.ar(sig, 1));
	sig = Pan2.ar(sig, pan).tanh;
	ReplaceOut.ar(bus, (sig * amp));
}).add;


// 5. Electric
// Dark synth based on chaotic Ugens
// example : e1 >> electric(oct=3, dur=16, amp=1, blur=2, vib=32).spread()


SynthDef(\electric, {
	arg bus=0,vib=1, amp=1, sus=1,blur=1, pan=0,gate=1, rel= 1, dur=1, freq=440;
	var sig, sig2, sig4, sig3, env;

	freq = In.kr(bus, 1);
	sus = sus * blur;

	sig =  Saw.ar(freq)*9504+ CuspN.ar(freq, 0.1)*0.00001;
	sig2 = Gendy5.ar(vib).lag/[2.01,3]/99++9;
	sig4 = LFNoise0.ar(1/2).lag+4/[2.01,3]/99++9;
	sig3 = sig.tanh;
	env =  EnvGen.ar(Env.linen(0.3,dur,0),doneAction:2);

	sig3 = CombN.ar(sig3, 1, (sig2/32) + sig4,9);
	sig3 = sig3.sum.tanh!2;

	sig3 = Mix(sig3) * 0.5;
	sig3 = Pan2.ar(sig3, pan);

	ReplaceOut.ar(bus, (sig3 * amp) * env);}).add;



// 6. Radio
// somekind of radio static/noise/chaotic
// r1 >> radio(oct=6, dur=2)


SynthDef(\radio, { |bus=0, freq=800, gate=1, amp=0.5, dur=0.25, pan=0, sus=1, blur=1|
	var env, son;

	freq = In.kr(bus, 1);
	sus = sus * blur;

	env = EnvGen.ar(Env.asr(0,1),gate,doneAction:2);
	 son =

			LFSaw.ar(freq, 0, Gendy4.ar(dur)) +
			LFNoise2.ar(freq) +
			Gendy5.ar(freq,8,10,32,freq * 4,
			Gendy5.ar(1, 0, SinOsc.ar(freq)),2, 0.5, 12);

	son = CombL.ar(son, 0.3, Dust.ar(0.5));
	son = Mix(son).tanh * 0.2;
	son = Limiter.ar(son);
	son = Pan2.ar(son, pan);

	son = son * env;

	ReplaceOut.ar(bus,Splay.ar(Pan2.ar(son * amp, pan)));

}).add;

// 7. DRONE
// to be used on lower freq

SynthDef(\drone, { arg bus = 0, speed = 1, amp = 0.5, pan=0, sus = 4, dur = 1, freq=200, gate=1, hpf=40, fmod=0, vib=0;
	var sig;
	var base_signal = LFNoise1;
    var adsr = EnvGen.ar(Env.linen(0.1,sus,0.1, 1, -3),gate,doneAction:2);
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	sig =  HPF.ar(
		FreeVerb2.ar(
			*XFade2.ar
			(SinOscFB.ar([freq,freq],base_signal.ar(speed*2)+1),
			 SinOscFB.ar([freq,freq + fmod],base_signal.ar(speed)+vib),base_signal.ar(120))),hpf);

	sig = LeakDC.ar((sig * 1.1).tanh, 0.999);
	sig = (sig * adsr) * amp;
	sig  = Mix(sig) * 0.4;
	sig = Limiter.ar(sig, 0.99);
	sig = Pan2.ar(sig * amp, pan);
	ReplaceOut.ar(bus, sig);
}).add;

// 8. TABLE
// Crazy table
SynthDef(\table, {
	arg gate=1, amp=0.5, bus=0, rel=1, pan=0, sus=1, blur=1, freq=440;
	var sig, env;

	freq = In.kr(bus, 1);
	sus = sus * blur;

	env = EnvGen.ar(Env.adsr(releaseTime: rel), gate, doneAction: 2);
	sig = {x=0;(80..100).do{|f|f=f/2;x=SinOsc.ar(f+[0,1],x*LFTri.kr(0.4,2).range(1.2,1.6))};x};
	sig = sig * env;
	sig = sig * amp;

	sig = Mix(sig) * 0.8;
	sig = Pan2.ar(sig, pan);

	ReplaceOut.ar(bus, Splay.ar(sig));
}).add;


// 9. The Filler
// plays fast stuff or a drumer depends on the mood, and settings
// o2 >> thefiller(dur=1, fmod=1)
// o2 >> thefiller(dur=1, fmod=4, vib=1)
// o2 >> thefiller(dur=1, fmod=4, vib=16)



SynthDef(\thefiller, {
	arg gate=1, amp=0.5, bus=0, rel=1, pan=0,fmod=128, freq=440, blur=1, sus=1, vib=0;
	var sig, env;
	freq = In.kr(bus, 1);
	sus = sus * blur;

	env = EnvGen.ar(Env.adsr(releaseTime: rel), gate, doneAction: 2);
	sig = {	{|i|Ringz.ar(LPF.ar(Impulse.ar(vib+4/(1.2+i)),1e4),1e3/(i+2),fmod+0.1)}
		.dup(20).scramble.sum.tanh};

	sig = Notch.ar(sig, 500, 0.8);
	sig = Notch.ar(sig, 400, 0.8);

	sig = (sig * env) * amp;
	sig = Mix(sig) * 0.4;
	sig = Pan2.ar(sig, pan).tanh;

	ReplaceOut.ar(bus, Splay.ar(sig));
}).add;


// 10. Garfield
// don't be scared
// a2 >> garfield(oct=2, dur=8, mult=[4, 4, 1, 1, 128, 128], vib=4, fmod=4, para1=0.

SynthDef(\garfield, { arg bus=0, freq=440, mult=4, amp=1, pan=0,gate=1, rel= 1, dur=1, phase=0, para1=0.1, vib=1, fmod=0;

	var env =  EnvGen.ar(Env.linen(0.0,dur,0),doneAction:2);
	var del =  SinOsc.ar(1/8, phase, mult);
	var sig =  SinOscFB.ar(freq, del, add: SinOsc.ar(vib));

	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

	sig = CrossoverDistortion.ar(sig, 0.8, para1);
	sig = RLPF.ar(sig, 3200, mul:0.1) + sig;
	sig = CombN.ar(sig, 0.04, 0.085);
	sig = Splay.ar(sig);

	sig = Mix(sig) * 1;
	sig = LeakDC.ar(Limiter.ar(sig, 1));
	sig = Pan2.ar(sig, pan).tanh;

	ReplaceOut.ar(bus, (sig * amp) * env);}).add;


////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
// III. DRUMS OR DRUM LIKE

// 1.CLICK
SynthDef(\click, { |amp = 0.25, freq = 42, bus=0, fmod=0,
	sus = 1, pan = 0|
	var sig;
	sig = BLowPass.ar(Impulse.ar(8,0,4), freq*10, 0.1);
	sig = sig + LFPar.ar(
		Env.perc(0,0.075).ar.linexp(0,1,freq, 1600) *
		LFDNoise3.kr(2).exprange(fmod.midiratio, 0.1.midiratio),
		-1);
	sig = sig * Env([1,0], [sus], -4).kr(2);
	sig = Mix(sig) * 1;
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus,Splay.ar( sig * amp ))
}).add;

////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
// IV PADS

// 1.Hoover
SynthDef( "hoover", {
|amp=0.1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, legatou =0.1, legatod = 1, gate=1|

var pwm, osc, env;

sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
freq = freq.lag(legatou,legatod);

freq = SinOsc.kr( { 2.9 rrand: 3.1 }!3, {2pi.rand}!3 ).exprange( 0.995, 1.005 ) * freq;
pwm = SinOsc.kr( {2.0 rrand: 4.0}!3 ).range(0.125,0.875);

// the saw/pulses
osc = (LFSaw.ar( freq * [0.25,0.5,1], 1 ).range(0,1)
               * (1 - LFPulse.ar(freq * [0.5,1,2], 0, pwm))).sum * 0.1;

// the bass
osc = osc + LFPar.ar( freq * 0.25, 0, 0.1 );

// eq for extra sharpness
osc = BPeakEQ.ar( osc, 6000, 1, 3 );
osc = BPeakEQ.ar( osc, 3500, 1, 6 );

// kind of chorus
osc = osc + CombC.ar( osc.dup, 1/200,
                       SinOsc.kr( 3, [0.5pi, 1.5pi] ).range(1/300,1/200),
               0.0 ) * 0.5;

env = EnvGen.kr( Env.asr, gate, doneAction:2 );

osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc*env*amp)}).add;

////////////////////////////////////////////////////////////////////////////////////////////
// fixed, best to be used with dur > 8, & sus = x1.dur/2, lower proc usage than ever.

(
SynthDef(\totalsin, {arg bus = 0, amp = 0.5, freq = 220, rel = 0.2, sus=1, hpf = 6000, pan = 0, fmod=0, blur=1;

	var sig , sig1, sig2, sig3, env;

	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

    sig1 = SinOscFB;
	sig2 = GVerb.ar(mean(FreqShift.ar(c=sig1.ar(sig1.ar(sig1.ar(freq/b=(1..9),1),1/b)+b*[freq-freq/2, freq, freq+freq/2],1),1/b)+c)/3,200,sus,0.5,0.5,9,1,0.7,1);
	sig = sig2 ;
	env=EnvGen.ar(Env(curve: 'lin',times: (sus * 2),levels: [0, amp, 0]), doneAction: 0);
	sig = sig * env;
	sig = sig * amp;
	sig = Mix(sig) * 0.6;
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus, sig);
}).add;
)

// 3. SynthWave
SynthDef(\synthWave, {
	arg bus=0, amp=0.5, freq=220,dur=1,vib=1, index=8,rel=8, blur=1, sus=1, pan=0, fmod=0;
	var env, sig, sig2;


	freq = In.kr(bus, 1);
	sus = sus * blur;

	freq = [freq, freq+fmod];

	env=EnvGen.ar(Env(curve: 'lin',times: (sus * 2),levels: [0, amp, 0]), doneAction: 0);

	sig =  SinOsc.ar(freq * 1, 0, freq * index * LFNoise1.kr(10.reciprocal).abs);
	sig2 = SinOsc.ar((freq * vib) + sig, 0, 1);

	sig = DelayN.ar(sig2, 0.048, 0.048);
	sig = Mix.arFill(5, { CombN.ar(sig, 0.1, LFNoise1.ar(Rand(0, 0.1), 0.001, 0.05), dur) });
	sig = AllpassN.ar(sig, 0.050, [Rand(0, 0.05), Rand(0,0.05)], 1)!3;
	sig = Mix(sig) * 0.5;
	sig = LPF.ar(sig, 20000);
	sig = LPF.ar(sig, 15000);
	sig = HPF.ar(sig,20);
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus, (sig * env) * amp);

}).add;



/////Cool with small dur, low CPU////
// 2. PROF

SynthDef("prof", {
	arg amp=0.3, pan=0, freq=0, vib=0, fmod=0, rate=8, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.5, sus=1, rel=0, peak=1, level=0.8, gate = 1, lforate = 10, lfowidth = 0.5, cutoff = 12000, rq = 0.5;

	var lfo, pulse, filter, env;
	lfo = LFTri.kr(lforate * [1, 1.01], Rand(0, 2.0) ! 2);
	pulse = Pulse.ar(freq * [1, 1.01], lfo * lfowidth + 0.5);
	filter = RLPF.ar(pulse, cutoff, rq);
	env = EnvGen.ar(
		envelope: Env.adsr(atk, decay, sus, rel, amp),
		gate: gate,
		doneAction: 2);
	Out.ar(bus, Pan2.ar(
		in: Mix(filter*amp*0.4) * env,
		pos: pan)
	);
}).add;




SynthDef(\pianovel, { |bus=0, amount=440, detune=0, gate=1, amp=0.5, velocity=127, hard=0.8, velhard=0.8|
	var son = MdaPiano.ar(amount + detune, gate, release: 0.9, stereo: 0.3, sustain: 0, vel: velocity, hard: hard, velhard: velhard);
	DetectSilence.ar(son, 0.01, doneAction:2);
	ReplaceOut.ar(bus, son * amp);
}).add;



SynthDef(\explosion2, {arg bus=0, freq = 200, pan=0.5, amp=0.5;
		var ae,sig,finalsig;
		ae = EnvGen.kr(Env.asr(0, 1, 0.05, 1, 0));
		sig = Impulse.ar(0);
		sig = LPF.ar(FreeVerb2.ar(sig,sig,1,0.95,0.4),freq);
		sig = (sig*5000).tanh;
		sig = LPF.ar(sig,8000);
		finalsig = amp*ae*sig;
		DetectSilence.ar(finalsig, doneAction:Done.freeSelf);
		ReplaceOut.ar(bus, finalsig);
}).add;




SynthDef(\ppad, {
	arg  sus,  amp, bus=0,gate=1;
	var sig, env, fenv;

	env=EnvGen.kr(Env([0,1,0],[1,6]),gate,timeScale:sus,doneAction:2);
	sig=SinOsc.ar(\freq.kr+LFNoise0.ar([400,160]).range(2,40).round(2));
	sig=sig+BPF.ar(PinkNoise.ar([0.4,0.6]),\freq.kr,0.1);
	sig=sig - sig.tanh;
	sig=sig*env*amp;
	ReplaceOut.ar(bus, sig);

}).add;



SynthDef(\pulseLead, { |bus=0, gate = 1, t_gate, amp = 1,
        freq = 080, i_prevFreq = -1,
        pwidth = 0.5, detun = 1.01, detunRand = 1.005, widthRand = 0.05, freqLag =
0.08, spread = 0.6,
        ffreq = 2000, gain = 1, t_panic = 0, ffDecay = 0.1, ffHeight = 0, acc = 0,
        atk = 0.01, dcy = 0.15, sus = 0.5, rel = 0.1, retrigLevel = 0.05|
        var n = 7,
        sig,
        detuneArray = Array.fill(n, { |i| detun ** (i / (n-1) * 2 - 1) }),
        ffreqEg = EnvGen.kr(Env.perc(0.01, ffDecay), gate) * (ffHeight * (acc >
0)),
        egTest = LocalIn.kr(1, 0), eg,
        retrig = t_gate * (egTest < retrigLevel);  // at trig time, are we below
retrigLevel?

        i_prevFreq = Select.kr(i_prevFreq < 0, [i_prevFreq, freq]);  // negative,
        freq = Select.kr(
                Duty.kr(Dseq([ControlDur.ir, Dseq([1], inf)]), 0, Dseq([1, Dseq([0],
inf)])),
                [freq, i_prevFreq]
        );
        freq = Lag.kr(freq, freqLag);

        sig = Pulse.ar(
                freq * detuneArray * Array.fill(detuneArray.size, {
                        TExpRand.kr(detunRand.reciprocal, detunRand, t_gate)
                }),
                Clip.kr(pwidth + Array.fill(detuneArray.size, {
                        TRand.kr(widthRand.neg, widthRand, t_gate)
                }), 0.01, 0.99)
        );
        sig = Splay.ar(sig.scramble, spread) * amp;

        ffreq = ffreq * (1 + ffreqEg);
        sig = MoogFF.ar(sig, Clip.kr(ffreq, 20, 20000), gain, t_panic);

        gate = (gate > 0) - (retrig > 0);
        eg = EnvGen.kr(Env.adsr(atk, dcy, sus, rel), gate, doneAction: 2);
        LocalOut.kr(eg, DC.kr(0));  // workaround for 3.8 bug
        sig = sig * eg;

        ReplaceOut.ar(bus, sig);
}).add;


SynthDef(\saw3, {
	arg atk=2, sus=0, rel=3, ts=1, c1=1, c2=(-1), freq=500, detune=0.2, pan=0, cfhzmin=4, cfhzmax=0.3, cfmin=500, cfmax=2000, rqmin=0.1, rqmax=0.2, lsf=200, ldb=0, amp=1, bus=0;
	var sig, env;
	env = EnvGen.kr(Env([0,1,1,0],[atk,sus,rel],[c1,0,c2]),timeScale:ts,doneAction:2);
	sig = Saw.ar(freq*{SinOsc.kr(0.1,detune).midiratio}!2) + VarSaw.ar(freq /2);
	sig = BPF.ar(
		sig,
		{LFNoise1.kr(
			LFNoise1.kr(4).exprange(cfhzmin,cfhzmax)
		).exprange(cfmin,cfmax)}!4,
		{LFNoise1.kr(0.1).exprange(rqmin,rqmax)}!4
	);
	sig = FreeVerb.ar(sig, 1, 40);
	sig = LPF.ar(sig, [300, 4300], 1);
	sig = BLowShelf.ar(sig,lsf,2,ldb);
	sig = Balance2.ar(sig[0],sig[1],pan);
	sig = sig*env*amp;
	ReplaceOut.ar(bus,sig);
}).add;



/// Pads long et beau// RATE & FMOD
/// h1 >> varicelle([0,5,3,2,9], dur=8, oct=(3,4,5), atk=PTri(5), rate=3, fmod=2, delay=(0,1,5), room=1, mix=0.5)
/// h2 >> varicelle(var([0,5,3,2,9],8), dur=1/2, sus=0.45, oct=[3,4,5], atk=.01, rate=0.3, fmod=0.15, delay=(0,1,5), room=1, mix=0.5) + (0,2,[4,3])
/// h3 >> varicelle(var([0,5,3,2,9],8), dur=1/2, oct=3, rate=2, fmod=5)

// Mod of «aurora borealis» by nicolaariutti

(
SynthDef.new(\varicelle,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, cutoff=5300, rel=0.01, peak=1, level=0.8, findex=0, frate=2|
var osc, oscl, oscr, sigA, sigB, sigC, env, modul;
sus = sus * blur;
freq = In.kr(bus, 1);

	modul = fmod * SinOsc.kr(rate, mul:0.5, add:0.5) * Line.kr(0, 1, 7);
		sigA = Pulse.ar(freq + modul, LFNoise2.kr(1).range(0.2, 0.8) );
		sigB = VarSaw.ar(freq + modul);
		sigC = WhiteNoise.ar() * 0.125;
		sigC = LPF.ar(sigC, freq*8);
	osc = SelectX.ar(LFNoise2.kr(2).range(0, 2), [sigA, sigB, sigC]);
	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
	osc = osc * amp * env;
	osc = Mix(osc) * 0.5;
	osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
)

//
// SynthDef(\coreNoiz, {
// 	|amp=1, pan=0, freq=0, vib=0, fmod=0, rate=8, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.001, sus=0.55,rel=0.125, peak=1, level=0.8, gate=1, lfofreq = 3, lopfreq = 800, rq = 0.5, detune1 = 12, detune2 = 8|
//
// 	var env, nvoices1=2, nvoices2=4, osc1, m, lfo, osc2, output;
//
// 	sus = sus * blur;
// 	freq = In.kr(bus, 1);
// 	freq = [freq, freq+fmod];
//
// 	env = EnvGen.ar(Env.adsr(atk, decay, sus, rel, amp), gate, doneAction:2);
//
// 	osc1 = {
// 		m = 2**(detune1/1200).rand2;
// 		lfo = SinOsc.ar(lfofreq.rand).range(0,1);
// 		DelayC.ar(LFSaw.ar(m * freq/2), 0.02, freq.reciprocal.rand * lfo);
// 	}.dup(nvoices1);
//
// 	osc2 = {
// 		m = 2**(detune2/1200).rand2;
// 		lfo = SinOsc.ar(lfofreq.rand).range(0,1);
// 		DelayC.ar(LFSaw.ar(m * freq), 0.02, freq.reciprocal.rand * lfo);
// 	}.dup(nvoices2);
//
// 	output = Pan2.ar(output*amp*env*0.1, pan);
// 	Out.ar(bus, output);
// }).add;

)
