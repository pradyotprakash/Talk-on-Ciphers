def repeatedXOR(string, key):
	count = 0
	keyLen = len(key)
	ret = ''
	for x in string:
		a = hex(ord(x) ^ ord(key[count % keyLen]))[2:]
		ret += '0' + a if len(a) == 1 else a
		count += 1

	return ret

print repeatedXOR("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", 'ICE')