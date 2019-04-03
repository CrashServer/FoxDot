from ..Buffers import *

class BeatStretchSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "stretch")
        self.pos = self.new_attr_instance("pos")
        self.sample = self.new_attr_instance("sample")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.base.append("osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * rate, startPos: BufSampleRate.kr(buf) * pos, loop: 1.0);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        return SampleSynthDef.__call__(self, pos, **kwargs)

stretch = BeatStretchSynthDef()
