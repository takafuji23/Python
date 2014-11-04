
def compress( _str ):
	comp_str = []
	count = 1

	comp_str.append(_str[0])
	for i in xrange(1, len(_str)):
		if _str[i] == _str[i-1]:
			count += 1
		else:
			if count != 1: 
				comp_str.append(str(count))
				comp_str.append(_str[i])
				count = 1
			else:
				comp_str.append(_str[i])

	if count != 1: 
		comp_str.append(str(count))
				

	return "".join(comp_str)

print compress(raw_input())

