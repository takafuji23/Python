
def is_anagram(_str1, _str2 ):
	if "".join(sorted(_str1)) == "".join(sorted(_str2)):
		return True
	else:
		return False

k = False

while k == False:
	_str1, _str2 = map(str, raw_input().split(" "))
	k = is_anagram(_str1, _str2)