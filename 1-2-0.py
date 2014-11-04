
def is_anagram(_str1, _str2 ):
	if len(_str1) != len(_str2):
		return False

	char_set1 = [0]*128
	char_set2 = [0]*128

	for i in _str1:
		char_set1[ord(i)] += 1 

	for i in _str2:
		char_set2[ord(i)] += 1


	for i, j in zip(char_set1, char_set2):
		if i != j:
			return False

	return True  

k = False

while k == False:
	_str1, _str2 = map(str, raw_input().split(" "))
	k = is_anagram(_str1, _str2)



