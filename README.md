# txhex2json

A small Python program that takes a Bitcoin transaction as an input in hex and parses it to output the transaction in JSON.

## Install

git clone this repo and ...

```
$ pip install pybitcointools
```

## Run

cd into this repo and execute txhex2json.py followed by a tx hex to see the json version of it:

```
$ ./txhex2json.py 0100000001b14bdcbc3e01bdaad36cc08e81e69c82e1060bc14e518db2b49aa43ad90ba260000000004A0048304402203f16c6f40162ab686621ef3000b04e75418a0c0cb2d8aebeac894ae360ac1e780220ddc15ecdfc3507ac48e1681a33eb60996631bf6bf5bc0a0682c4db743ce7ca2bab01ffffffff0140420f00000000001976
```

## Tests

```
$ python ./test.py
```
