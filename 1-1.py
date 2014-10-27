
def is_unique_chars2( _str ):
	if len(_str) > 256:
		return False

	char_set = [0]*256
	for i in _str:
		print i
		if char_set[ord(i)]:
			return False

		char_set[ord(i)] = True
	return True

j = True

while j:
	_str = raw_input()
	j = is_unique_chars2(_str)
