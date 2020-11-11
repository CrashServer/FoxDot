/*
This SynthDef is especially cool to me, because working on effects for guitars is what ended
up getting me into supercollider in the first place, and now in a continuation of that weird
chain of events, I've come full circle to making a clean guitar sound in supercollider!

This model can be broken into separate sections based on the parts of an electric guitar: It
starts with a plucked string made using modal synthesis, and that goes into a single pickup.
The pickup's position is modeled in the modal synthesis portion, and the electronic components
of the pickup (as well as the volume and tone controls) are modeled afterwards with filters.

The frequencies of each mode on the vibrating guitar string are determined by a standard stiff
string model in freqArray, where 0.00001 is a constant stretching these frequencies a tiny bit
from the harmonic series. Similarly, the decay times of each mode are found by decArray, where
decayCoef and dampCoef (which is best left low) control the apparent brightness of each note.

In ampArray, the first line works like an anti-aliasing filter, and the second line models the
string being plucked at different locations, from the bridge at pickPos = 0 to the nut at
pickPos = 1. Everything else inside ampArray, as well as the line after it, model a pickup
with a certain width (parallel to the string) and position, once again from the brigde at
pickupPos = 0 to the nut at pickupPos = 1. The pickup width is not, however, a ratio from 0 to
1, but pickupWidth is instead measured in inches. This gets turned into a ratio by dividing it
by the scale length of the guitar, which I set to 25.5 inches. This isn't a variable control
because the main effects it has on a real guitar are on the ratios for each of the parameters
I just mentioned, making it redundant to control. Lastly, the open frequency of a string (the
note it's tuned to, as in e-a-d-g-b-e) has some effect when it interacts with the position of
the pickup. Looking at the demo, you'll see I used that to write in what string a note is
being played on.

After all the complicated modal stuff, it's kind of interesting that the circuitry of a guitar
from the pickups to any passive controls to a cable and output load can all be modeled pretty
well with a resonant low pass filter. Rather than figure out a bunch of variables for the
number of turns in the pickup windings, the pickup's capacitance, and everything else inside a
guitar, all you get are the filter's resonant frequency and rq. There's another low pass filter
for you that I labeled tone after a guitar control. I set it a bit lower than the resonant
filter to roughly match an experimentally-determined filter curve I found.

After that is a quick way of approximating muting a vibrating string with one hand. You can
control when that happens with muteSus. If it's longer than rel, you'll let the string ring
out. You'll see in the demo that I mute a string just before playing a new note on it, which
helps with the realism, just like waving pickPos around slightly. What helps the most, however,
is starting the demo with an add9 chord, as every guitar demo should start.

By Josh Mitchell August 2020.
*/
(
SynthDef(\bassguitar, {
	// Standard values
	|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.01, rel=0.01, pick=0.414, rq = 0.5, cutoff = 250|

	var exciter, freqArray, ampArray, decArray, constant, mute, snd, openFreq, pickupPos, pickupWidth, decayCoef, dampCoef;
	openFreq = 82.5;
	pickupPos = 17*decay;
	pickupWidth = 0.75;
	decayCoef = 0.125;
	dampCoef = 0.0002;

	sus = sus*blur;
	freq = In.kr(bus, 1);
	freq = freq/4;
	freq = [freq, freq+fmod];
	// Make a Constant from pickupWidth for ampArray
	constant = pickupWidth/25.5; // The scale length is set to 25.5 inches
	constant = constant * pi/2;
	constant = constant/82.5;

	// Stiff String Model for Frequencies
	freqArray = Array.fill(50, {
		arg i;
		(i + 1) * sqrt(1 + ((i + 1).pow(2) * 0.00001))
	});
	freqArray = freqArray/freqArray[0];

	// Decay Times
	decArray = Array.fill(50, {
		arg i;
		exp(
			(-1 * i)/
			(
				(1/decayCoef) +
				((dampCoef/10) * freq.pow(2)) +
				(dampCoef * freqArray[i].pow(2))
		    )
		)
	});
	decArray = decArray/decArray[0];

	// Rescale freqArray for ampArray and Klank
	freqArray = freqArray * freq;

	// Effects of Pick Position and Pickup Placement
	ampArray = Array.fill(50, {
		arg i;
		((1 - ((freqArray[i] - 19000)/1000).tanh)/2) *
		sin(((i + 1) * pi) * pick) *
		(
			sin(pi * pickupPos * freqArray[i]/openFreq) *
			(
			    (
					sin(constant * freqArray[i])/
					(constant * freqArray[i])
				) - cos(constant * freqArray[i])
			)
		)/(freqArray[i].pow(2))
	});
	ampArray = ampArray * 2/(constant.pow(2));

	// The Pick
	exciter = Impulse.ar(0) * 1;

	// The String
	snd = Klank.ar(
		specificationsArrayRef:
		    Ref.new([freqArray, ampArray, decArray]),
		input: exciter,
		decayscale: sus*2 + rel
	);

	snd = Mix.ar(snd);

	// The Pickup
	snd = RLPF.ar(
		in: snd,
		freq: cutoff,
		rq: rq);

	snd = LPF.ar(
		in: snd,
		freq: 250);

	// An Envelope for Muting the String
	mute = Env.new(
		levels: [1, 1, 0, 0],
		times: [rel+sus, 0.05, 0.01]).ar(doneAction: 2);

	// Mute the String
	snd = LPF.ar(
		in: snd,
		freq: LinExp.ar(
			in: mute,
			srclo: 0, srchi: 1,
			dstlo: 20, dsthi: 20000));

	// Output Stuff
	snd = snd * amp;
	snd = snd.tanh;
	snd = LeakDC.ar(snd);
	snd = Limiter.ar(snd);

	//DetectSilence.ar(in: snd, doneAction: 2);

	ReplaceOut.ar(bus, Pan2.ar(snd, pan));
},
metadata: (
	credit: "by Josh Mitchell",
	category: \guitar,
	tags: [\pitched, \modal]
)
).add;)