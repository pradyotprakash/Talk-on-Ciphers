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

# code to test out the implementation
if __name__ == '__main__':
	plaintext = "WELCOMETOTHESESSIONONCIPHERS"
	K = 3

	ciphertext = encrypt(plaintext, K)
	print 'Ciphertext: %s'%ciphertext

	recoveredPlaintext = decrypt(ciphertext, K)
	print 'Plaintext:  %s'%recoveredPlaintext