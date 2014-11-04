
def convert_to_zero( matrix ):
	raw_with_zero = []
	col_with_zero = []

	for i,raw in enumerate(matrix):
		for j,value in enumerate(raw):
			if value == 0:
				raw_with_zero.append(i)
				col_with_zero.append(j)

	max_raw = i + 1
	max_col = j + 1

	# print "max", max_raw, max_col

	raw_with_zero = sorted(list(set(raw_with_zero)))
	col_with_zero = sorted(list(set(col_with_zero)))

	# print "aaa", raw_with_zero, col_with_zero

	for i in range(max_raw):
		for j in range(max_col):
			# print "ccc", i, j
			if i in raw_with_zero or j in col_with_zero:
				# print "bbb", i, j
				matrix[i][j] = 0

	return matrix

matrix = [[1,2,3,4,5],[1,2,3,4,0],[0,2,3,4,5],[1,2,0,4,5],[1,2,3,4,5],[1,2,3,4,0]]
print convert_to_zero(matrix)


