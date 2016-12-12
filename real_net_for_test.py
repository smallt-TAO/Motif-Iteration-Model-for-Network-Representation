"""
  This time I will check the origin AI for complex networks.
  __author__ = 'Smalltao'
  """

from scipy.misc import imsave
from numpy import *
from algorithm import matrix_random
from algorithm import matrix_change


def handle_data(num, st):
	matrix_data = [([0] * num) for si in range(num)]
	fr = open(st + ".txt")
	for eachLine in fr:
		line = eachLine.strip().split()
		(m, n) = (int(line[0]) - 1, int(line[1]) - 1)
		matrix_data[m][n] = 1
		matrix_data[n][m] = 1
	imsave(st + "_old.png", matrix_data)
	matrix_data = matrix_random(matrix_data)
	matrix_data = matrix_change(matrix_data)
	imsave(st + ".png", matrix_data)


def handle_data0():
	st = "G:\\code_Python\\see_network\\test_data\\SmaGri"
	num = 1059
	matrix_data = [([0] * num) for si in range(num)]
	fr = open(st + ".txt")
	for eachLine in fr:
		line = eachLine.strip().split()
		for j in range(1, len(line)):
			(m, n) = (int(line[0]) - 1, int(line[j]) - 1)
			matrix_data[m][n] = 1
			matrix_data[n][m] = 1
	imsave(st + "_old.png", matrix_data)
	matrix_data = matrix_random(matrix_data)
	matrix_data = matrix_change(matrix_data)
	imsave(st + ".png", matrix_data)


if __name__ == "__main__":
	s1 = "G:\\code_Python\\see_network\\test_data\\Jazz"
	handle_data(198, s1)
	handle_data0()
