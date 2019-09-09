from random import choice as choose

if __name__ != "__main__":

    from ..SCLang   import SynthDef, SynthDefs
    from ..Players  import Player
    from ..Patterns import Sequences
    from ..Buffers import alpha, nonalpha
    from ..Patterns.Sequences import *
    from ..Effects.Util import FxList

    from types import FunctionType

    #PATTERN LIST
    patternNames = {name: obj for name, obj in vars(Sequences).items() \
                if (type(obj) == FunctionType and name.startswith("P"))}

    #SYNTH LIST
    synthdefNames = [i for i in SynthDefs][5:]

    #FX LIST
    fxNames = [x for x in FxList.keys()]

    # To ignore    
    del patternNames['PSq']
    del patternNames['PPairs']
    del patternNames['PSine']
    del patternNames["Pow"]
    del patternNames["PEq"]
    del patternNames["PNe"]
    del patternNames["PulsesToDurations"]
    del patternNames["PatternMethod"]
    del patternNames["PatternFormat"]
    del patternNames["PEuclid2"]
    del patternNames["PZip2"]
    del patternNames["PJoin"]
    del patternNames["PBeat"]
    del patternNames["PDelay"]

    synthdefNames.remove("video")
    fxNames.remove("fx1")
    fxNames.remove("fx2")
    
# Grammar

from random import random, randint
import re
from inspect import signature

re_player=r"\w+"
re_synthdef=r"\w+"
re_args=r".+"
re_methods=r".?" # todo

re_degree = re.compile(r"([\w()[\], /]*)\s*(?!\w*=)")
re_kwargs = re.compile(r"(\w+=" + re_degree.pattern + ")")

re_input = r"(?:\s*)(?P<player>{player}) >> (?P<synthdef>{synthdef})\((?P<args>{args})?\)(?P<methods>{methods})?"
re_input = re_input.format(player=re_player, synthdef=re_synthdef, args=re_args, methods=re_methods)
re_input = re.compile(re_input)

def createPlayer(**kwargs):

    player   = kwargs['player']
    synthdef = kwargs['synthdef']
    
    degree   = str(kwargs.get("degree", ""))
    methods  = kwargs.get("methods", "")
    keywords = format_kwargs(kwargs.get("kwargs", ""))

    sentence = "{player} >> {synthdef}({degree}" + (", " if (len(degree) > 0 and len(keywords) > 0) else "") + "{keywords}){methods}"
    
    return sentence.format(player=player, synthdef=synthdef, degree=degree, methods=methods, keywords=keywords)

def getArgs(s):
    degree, kwargs = "", {}
    # Find degree
    match = re_degree.match(s)
    if match:
        degree = match.group(0)
        if degree.endswith(","): degree = degree[:-1]
        s = s[match.end():]
    # Find kwargs
    match = re_kwargs.findall(s)
    if match:
        for g1, g2 in match:
            if g1.endswith(","): g1 = g1[:-1]
            key, value = g1.split("=")
            kwargs[key] = value
    return degree, kwargs

def playerData(s):
    ''' Returns a list of tuples of original string and dict of values '''
    p = []
    i = 0
    while True:
        match = re_input.match(s, pos=i)
        if match is None:
            return p
        else:
            d = match.groupdict()
            if d['args'] is not None:
                d['degree'], d['kwargs'] = getArgs(d['args'])
            else:
                d['degree'], d['kwargs'] = "", {}
            del d['args']
            p.append((match.group().strip(), d))
            i = match.end()
    return

def format_kwargs(d):
    return ", ".join( ["{}={}".format(*item) for item in sorted(d.items(), key=lambda x: str(x[0]))] )

# Generic actions

def GENERATE_PATTERN(keyword=None):

    pat = choose(list(patternNames.values()))
    n = len(signature(pat).parameters)
    if pat.__name__ not in patternInputs:
        args = [str(GENERATE_INTEGER(keyword)) for i in range(n)]
    else:
        args = []
        for i in range(n):
            args.append( str(patternInputs[pat.__name__][i](keyword)) )        
    return pat.__name__ + "({})".format(", ".join(args))

def GENERATE_LIST(keyword=None):
    return '[{}]'.format(", ".join([str(GENERATE_NUMBER(keyword)) for n in range(randint(2,9))]))

def GENERATE_TUPLE(keyword=None):
    return '({})'.format(", ".join([str(GENERATE_INTEGER(keyword)) for n in range(randint(2,3))]))

def GENERATE_INTEGER(keyword=None):
    if random() > 0.9:
        return str(randint(7,19))
    else:
        return str(randint(1,9))

def GENERATE_NUMBER(keyword=None, _min=1, _max=9):
    ''' Return a random number or fraction '''
    if random() > 0.5 and keyword != "amp":
        return randint(_min,_max)
    elif keyword == "amp":
        a = randint(_min, _max)
        b = randint(a, a*3)
        return str(a) + "/" + str(b)
    else:
        return str(randint(max(_min, 1),_max)) + "/" + str(randint(max(_min, 1),_max))

def GENERATE_NOTHING(keyword=None):
    return " "

def GENERATE_RDM(keyword=None):
    return str(round(random(),2))

def GENERATE_FREQLIST(keyword=None):
    freq1 = []
    return 'linvar([{},{}],{})'.format(str(randint(300, 12000)),str(randint(300, 12000)),GENERATE_LIST())

def GENERATE_FX():
    fx_rnd =  choice([x for x in fxNames])
    if fx_rnd in fx_integer:
        fx_arg = GENERATE_PATTERN() 
    elif fx_rnd in fx_freq:
        fx_arg = GENERATE_FREQLIST()
    else:
        fx_arg = str(round(random(),2))    
    return str(fx_rnd) + "=" + fx_arg

def GENERATE_CHAR():
    rnd_char_list = []
    clr_list = ["1","2","3","4","?","!"] 
    clr_nonalpha = [x for x in nonalpha.keys()]
    for i in clr_list:
        clr_nonalpha.remove(i)
    for i in range(randint(3,10)):
        if random() > 0.3:
            if random() > 0.5:
                rnd_char_list.append(choice(list(clr_nonalpha)))
            else:
                rnd_char_list.append(choice(list(alpha.upper())+list(alpha))) 
        else:
            rnd_char_list.append(".")               
    return "".join(rnd_char_list)    

def GEN_CHOOSE_VALUE(keyword=None):
    r = random()
    # Choose between existing pattern
    if 0.00 <= r <= 0.33:
        return GENERATE_PATTERN(keyword)
    # Randomly generated list of numbers
    if 0.33 <= r <= 0.66:
        if random() > 0.25 or keyword == "dur":
            return GENERATE_LIST(keyword)
        else:
            return GENERATE_TUPLE(keyword)
    # Single value
    if 0.66 <= r <= 1.00:
        return GENERATE_NUMBER(keyword)

def GEN_CHANGE_VALUE(value, keyword=None):
    value = str(value)
    match = list(re.finditer(r"\d+(?:[/.]\d+)?", value))
    if len(match) == 1:
        return value[:match[0].start()] + str(GENERATE_NUMBER(keyword)) + value[match[0].end():]
    i = 0
    out = []
    for num in match:
        j = num.start() 
        new_num = str(GENERATE_NUMBER(keyword)) if random() > 0.5 else num.group()
        out += [value[i:j], new_num]
        i = num.end()
    out.append(value[i:])
    return "".join(out)

# Actions

def ADD_NEW_KWARG(*args, **kwargs):
    new_kw = [kw for kw in Keywords if kw not in kwargs['kwargs']]
    if len(new_kw) > 0:
        if "dur" not in new_kw and random() > 0.25:
            new_kw = "dur"
        else:
            new_kw = choose(new_kw)
        kwargs['kwargs'][new_kw] = GEN_CHOOSE_VALUE(new_kw)
    return kwargs

def CHANGE_DEGREE(*args, **kwargs):
    ''' Randomly generates a new degree, or edits some of the previous values '''
    if len(str(kwargs['degree'])) or random() > 0.5:
        # generate new
        kwargs['degree'] = GEN_CHOOSE_VALUE('degree')
    else:
        kwargs['degree'] = GEN_CHANGE_VALUE(kwargs['degree'], 'degree')
    return kwargs

def CHANGE_KWARG(*args, **kwargs):
    if kwargs['kwargs']:
        kw, value = choose(kwargs['kwargs'].items())
        if random() > 0.5:
            kwargs['kwargs'][kw] = GEN_CHANGE_VALUE(value, kw)
        else:
            kwargs['kwargs'][kw] = GEN_CHOOSE_VALUE(value)
    else:
        kwargs = ADD_NEW_KWARG(*args, **kwargs)
    return kwargs

def ADD_NEW_METHOD(*args, **kwargs):
    return kwargs

# Patterns that take patterns as input

_pat = lambda keyword: choose([GENERATE_PATTERN, GENERATE_LIST]).__call__(keyword)
_int = GENERATE_INTEGER
_num = GENERATE_NUMBER
_tuple = GENERATE_TUPLE
_list = GENERATE_LIST
_rdm = GENERATE_RDM
_null = GENERATE_NOTHING

patternInputs = {
    'PStutter' : [_pat, _int],
    'PShuf'    : [_pat],
    'PAlt'     : [_pat, _pat, _pat],
    'PStep'    : [_int, _num, _num],
    'PSum'     : [_int, _num, _null],
    'PStretch'  : [_pat, _int],
    'PZip'     : [_pat, _pat, _pat],
    'PRhythm'  : [_tuple],
    'PBern'    : [_int, _rdm],
    'PDur'     : [_int, _int, _int, _list]
                 }

fx_integer = ["coarse", "striate", "crush", "chop", "tremolo", "spin", "formant", "leg", "squiz", "triode"]
fx_freq = ["hpf", "lpf", "bpf", "spf", "mpf" ]

# Constants

def WeightedList(weights):
    data = []
    for item, weight in weights.items():
        data += ([item] * weight)
    return data    

Players = [ "g1", "g2", "g3", "g4", "g5" ]

ActionWeights = { ADD_NEW_KWARG  : 2,
                  CHANGE_DEGREE  : 5,
                  CHANGE_KWARG   : 3,
                  ADD_NEW_METHOD : 0 }

Actions = WeightedList(ActionWeights)

KeywordWeights = { "dur"   : 4,
                   "amp"   : 1,
                   "vib"   : 1,
                   "sus"   : 1,
                   "chop"  : 1,
                   "bits"  : 1,
                   "delay" : 1,
                   "pan"   : 1 }

Keywords = WeightedList(KeywordWeights)
