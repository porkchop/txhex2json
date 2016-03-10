#!/usr/bin/python

import sys
from itertools import izip

# Tx Nibbles Size Constants
version_nibbles = 8
locktime_nibbles = 8

# Input Nibbles Constants
prev_txhash_nibbles = 64
prev_out_index_nibbles = 8
sequence_nibbles = 8

# Output Nibbles Constants
value_nibbles = 16

def reverse_bytes(buf):
    return "".join(reversed([buf[i:i+2] for i in range(0, len(buf), 2)]))
    
def read_int(buf):
    buf = reverse_bytes(buf)
    return int(buf, 16)

def read_var_int(buf):
    flag_byte = buf[:2]
    if flag_byte == 'FD':
        return read_int(buf[2:2]), 6
    if flag_byte == 'FE':
        return read_int(buf[2:4]), 10
    if flag_byte == 'FF':
        return read_int(buf[2:8]), 18
    else:
        return read_int(buf[:2]), 2

def read_input(buf):
    inp = {
        'outpoint': {
            'hash': reverse_bytes(buf[:prev_txhash_nibbles]),
            'index': read_int(buf[prev_txhash_nibbles:prev_txhash_nibbles + prev_out_index_nibbles])
        }
    }
    
    index = prev_txhash_nibbles + prev_out_index_nibbles
    script_len, nibbles_read = read_var_int(buf[index:])
    index += nibbles_read
    inp['script'] = buf[index:index + 2 * script_len]
    index += 2 * script_len
    inp['sequence'] = read_int(buf[index:index + sequence_nibbles])

    return inp, index + sequence_nibbles

def read_output(buf):
    out = {
        'value': read_int(buf[:value_nibbles])
    }
    
    index = value_nibbles
    script_len, nibbles_read = read_var_int(buf[index:])
    index += nibbles_read
    out['script'] = buf[index:index + 2 * script_len]

    return out, index + 2 * script_len

def convert(txhex):
    tx = {
        'version': read_int(txhex[:version_nibbles]),
        'ins': [],
        'outs': [],
        'locktime': read_int(txhex[-locktime_nibbles:])
    }
    
    num_ins, nibbles_read = read_var_int(txhex[version_nibbles:])
    index = version_nibbles + nibbles_read
    
    for i in range(0, num_ins):
        inp, nibbles_read = read_input(txhex[index:])
        index += nibbles_read
        tx['ins'].append(inp)
    
    num_outs, nibbles_read = read_var_int(txhex[index:])
    index += nibbles_read
    
    for i in range(0, num_outs):
        out, nibbles_read = read_output(txhex[index:])
        index += nibbles_read
        tx['outs'].append(out)
        
    return tx

def __main__(argv):
    if len(argv) == 0:
        print 'Usage: txhex2json <txhex>'
    else:
        print convert(argv[0])

if __name__ == "__main__":
    __main__(sys.argv[1:])
