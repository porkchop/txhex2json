import txhex2json

txhex = '0100000001b14bdcbc3e01bdaad36cc08e81e69c82e1060bc14e518db2b49aa43ad90ba260000000004A0048304402203f16c6f40162ab686621ef3000b04e75418a0c0cb2d8aebeac894ae360ac1e780220ddc15ecdfc3507ac48e1681a33eb60996631bf6bf5bc0a0682c4db743ce7ca2bab01ffffffff0140420f00000000001976a914660d4ef3a743e3e696ad990364e555c271ad504b88ac00000000'
expected = {'locktime': 0, 'outs': [{'value': 1000000, 'script': '76a914660d4ef3a743e3e696ad990364e555c271ad504b88ac'}], 'version': 1, 'ins': [{'script': '0048304402203f16c6f40162ab686621ef3000b04e75418a0c0cb2d8aebeac894ae360ac1e780220ddc15ecdfc3507ac48e1681a33eb60996631bf6bf5bc0a0682c4db743ce7ca2bab01', 'outpoint': {'index': 0, 'hash': '60a20bd93aa49ab4b28d514ec10b06e1829ce6818ec06cd3aabd013ebcdc4bb1'}, 'sequence': 4294967295}]}
result = txhex2json.convert(txhex)

assert result == expected

print "Decoding works"
