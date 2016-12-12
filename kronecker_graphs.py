import math
__author__ = 'Smalltao'


def kronecker_graphs(i_matrix, n):
	"""
	:param i_matrix: init matrix of begin.
	:param n: iter num of the net work
	"""
	# init the matrix
	m = len(i_matrix)
	k = int(math.log(n, m))
	for i in range(1, k):
		size = m ** (i + 1)
		if i == 1:
			it_matrix = i_matrix
		else:
			it_matrix = iter_matrix

		iter_matrix = [([0] * size) for si in range(size)]
		for iter_i in range(len(it_matrix)):
			for iter_j in range(len(it_matrix)):
				if it_matrix[iter_i][iter_j] == 1:
					for ii in range(m):
						for jj in range(m):
							iter_n = int(m)
							iter_matrix[iter_i * iter_n + ii][iter_j * iter_n + jj] = i_matrix[ii][jj]
		it_matrix = iter_matrix

	if len(it_matrix) < n:
		final_matrix = [([0] * n) for si in range(n)]
		for i in range(len(it_matrix)):
			for j in range(len(it_matrix)):
				final_matrix[i][j] = it_matrix[i][j]
		it_matrix = final_matrix

	return it_matrix
