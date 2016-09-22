def encrypt(message, key):
	"""Encrypt the plaintext using caesar cipher"""
	numericRepresentation = []
	for c in message:
		numericRepresentation.append(ord(c) - 65)

	cipher = ""
	for x in numericRepresentation:
		cipher += chr((x + key) % 26 + 65)

	return cipher

def decrypt(cipher, key):
	"""Decrypt the ciphertext encrypted using caesar cipher"""
	numericRepresentation = []
	for c in cipher:
		numericRepresentation.append(ord(c) - 65)

	message = ""
	for x in numericRepresentation:
		message += chr((x - key) % 26 + 65)

	return message

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

def calculateScoreForCharacters(text):
	lowerCaseString = text.lower()
	
	score = 0.0
	for i in range(len(lowerCaseString)):
		c = lowerCaseString[i]
		score = score + charFrequencies[c]

	return score

def breakCipher(cipher):
	bestGuess = -1.0
	bestKey = 0

	for i in range(1, 10):
		guessKey = i
		probablePlaintext = decrypt(cipher, guessKey)
		scoreOfGuess = calculateScoreForCharacters(probablePlaintext)

		if scoreOfGuess > bestGuess:
			bestGuess = scoreOfGuess
			bestKey = guessKey

	print 'Best key: %s'%bestKey
	return decrypt(cipher, bestKey)

if __name__ == '__main__':
	plaintext = "WELCOMETOTHESESSIONONCIPHERS"
	cipher = encrypt(plaintext, 7)

	broken = breakCipher(cipher)
	print 'Recovered plaintext: %s'%broken