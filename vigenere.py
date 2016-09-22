def encrypt(message, key):
	"""Encrypt the plaintext using caesar cipher"""
	numericRepresentationForMessage = []
	numericRepresentationForKey = []
	
	for c in message:
		numericRepresentationForMessage.append(ord(c) - 65)

	for c in key:
		numericRepresentationForKey.append(ord(c) - 65)

	cipher = ""
	l = len(key)
	for i in range(len(numericRepresentationForMessage)):
		cipher += chr((numericRepresentationForMessage[i] + numericRepresentationForKey[i%l]) % 26 + 65)

	return cipher


def decrypt(cipher, key):
	"""Decrypt the ciphertext encrypted using caesar cipher"""
	numericRepresentationForMessage = []
	numericRepresentationForKey = []
	
	for c in cipher:
		numericRepresentationForMessage.append(ord(c) - 65)

	for c in key:
		numericRepresentationForKey.append(ord(c) - 65)

	message = ""
	l = len(key)
	for i in range(len(numericRepresentationForMessage)):
		message += chr((numericRepresentationForMessage[i] - numericRepresentationForKey[i%l]) % 26 + 65)

	return message


# code to test out the implementation
if __name__ == '__main__':
	plaintext = "ILOVECRYPTO"
	K = "WNCC"

	ciphertext = encrypt(plaintext, K)
	print 'Ciphertext: %s'%ciphertext

	recoveredPlaintext = decrypt(ciphertext, K)
	print 'Plaintext:  %s'%recoveredPlaintext