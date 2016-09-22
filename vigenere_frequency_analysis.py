charFrequencies = {'a': 0.0651738,
					'b': 0.0124248,
					'c': 0.0217339,
					'd': 0.0349835,
					'e': 0.1041442,
					'f': 0.0197881,
					'g': 0.0158610,
					'h': 0.0492888,
					'i': 0.0558094,
					'j': 0.0009033,
					'k': 0.0050529,
					'l': 0.0331490,
					'm': 0.0202124,
					'n': 0.0564513,
					'o': 0.0596302,
					'p': 0.0137645,
					'q': 0.0008606,
					'r': 0.0497563,
					's': 0.0515760,
					't': 0.0729357,
					'u': 0.0225134,
					'v': 0.0082903,
					'w': 0.0171272,
					'x': 0.0013692,
					'y': 0.0145984,
					'z': 0.0007836,
					' ': 0.1918182 }

import itertools, caesar_frequency_analysis

data = "EYQXAPTALGQ"

def distance(s1, s2):
	# assume len(s1) == len(s2)
	d = 0
	for (x,y) in zip(s1, s2):
		c1 = ord(x) - 65
		c2 = ord(x) - 65

		d = d + (c1 - c2)%26

	return d

def normalizedDistance(data, keysize):

	blocks = [data[i:i+keysize] for i in range(0, len(data), keysize)][0:4]
	combinations = list(itertools.combinations(blocks, 2))
	distances = [distance(entry[0], entry[1]) for entry in combinations][0:6]
	
	return float(sum(distances))/(float(len(distances)) * keysize)

def breakVigenereCipher(data, maxKeySize):
	keysizes = range(2, maxKeySize)
	keysizes.sort(key=lambda x:normalizedDistance(data, x))

	keysizes = keysizes[0:1]

	for keysize in keysizes:
		print keysize
		blocks = [data[i:i+keysize] for i in range(0, len(data), keysize)]
		transpose = list(itertools.izip_longest(*blocks, fillvalue='0'))

		decrypted = [caesar_frequency_analysis.breakCipher(t) for t in transpose]
		decrypted = list(itertools.izip_longest(*decrypted, fillvalue='0'))

		return ''.join([''.join(d) for d in decrypted])
		

if __name__ == '__main__':
	print breakVigenereCipher(data, 10)