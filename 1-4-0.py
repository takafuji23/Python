
def space_replace( _str):
	str_lists = list(_str)
	for i,str_list in enumerate(str_lists):
		if str_list == " ":
			str_lists[i] = "%20"
	return "".join(str_lists)

_str = raw_input()
print space_replace(_str)


