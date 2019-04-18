#!/usr/bin/python

"""

FoxDot is a Python library and programming environment that provides a fast and 
user-friendly abstraction to the powerful audio-engine, SuperCollider. It comes 
with its own IDE, which means it can be used straight out of the box; all you need 
is Python and SuperCollider and you're ready to go!

For more information on installation, check out [the guide](http://foxdot.org/installation), 
or if you're already set up, you can also find a useful starter guide that introduces the
key components of FoxDot on [the website](http://foxdot.org/).

Please see the [documentation](http://docs.foxdot.org/) for more detailed information on 
the FoxDot classes and how to implement them.

Copyright Ryan Kirkbride 2015
"""

from __future__ import absolute_import, division, print_function

import os

import subprocess

try:
    import psutil
except:
    os.system("pip install psutil")

try:
    import getpass
except:
    print("Couldn't import getpass library")

username = getpass.getuser()

def is_proc_running(name):
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        #print(p);
        procname = p.info['name'] or \
             p.info['exe'] and os.path.basename(p.info['exe']) == name or \
             p.info['cmdline'] and p.info['cmdline'][0] == name
        if(procname.startswith(name)):
            return True
    return False


running = (is_proc_running("sclang"))

if(running == False):
    
    subprocess.Popen(["C:\Program Files\SuperCollider-3.10.2\sclang.exe", "C:/Users/"+username+"/Desktop/FoxDot-master/startup.scd"], cwd="C:\Program Files\SuperCollider-3.10.2", shell=True)

from .lib import *


def main():
    """ Function for starting the GUI when importing the library """
    FoxDot = Workspace.workspace(FoxDotCode).run()

def Go():
    """ Function to be called at the end of Python files with FoxDot code in to keep
        the TempoClock thread alive. """
    try:
        import time
        while 1:
            time.sleep(100)
    except KeyboardInterrupt:
        return

