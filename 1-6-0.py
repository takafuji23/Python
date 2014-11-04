
def rotate(matrix, n):
	layer = 0
	while layer < n/2:
		first = layer
		last = n - 1 - layer
		i = first
		print "First", i, first, last
		while i < last:
			offset = i - first
			print "Second", i, first, last, offset
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
			i += 1

		layer += 1

	return matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print rotate(matrix, 4)