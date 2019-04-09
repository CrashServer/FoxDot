from ..Buffers import *

class BeatStretchSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "stretch")
        self.pos = self.new_attr_instance("pos")
        self.index = self.new_attr_instance("index")
        self.sample = self.new_attr_instance("sample")
        self.dur = self.new_attr_instance("dur")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['dur']   = 4
        self.defaults['index']   = 0
        self.base.append("osc = LoopBuf.ar(1, buf, BufFrames.kr(buf) / (dur*44100), gate: 1, startPos: BufFrames.kr(buf) * (1-(index/2)), startLoop: BufFrames.kr(buf) * (1-(index/2)), endLoop: BufFrames.kr(buf) * (index/2), interpolation: 2);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        return SampleSynthDef.__call__(self, pos, **kwargs)

stretch = BeatStretchSynthDef()
