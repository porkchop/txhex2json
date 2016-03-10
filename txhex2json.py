#!/usr/bin/python

import sys
from pybitcointools import *

def convert(txhex):
    return deserialize(txhex)

def __main__(argv):
    if len(argv) == 0:
        print 'Usage: txhex2json <txhex>'
    else:
        print convert(argv[0])

if __name__ == "__main__":
    __main__(sys.argv[1:])
