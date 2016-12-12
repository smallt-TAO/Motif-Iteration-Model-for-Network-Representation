"""
This part code for the big image to small image
for the social network can be fit for the CNN
that we did train.
"""
from algorithm import matrix_random
from algorithm import matrix_change
from feature_matrix import average_feature
from feature_matrix import degree_distribution
from scipy.misc import imsave
import scale_free_ba
import ncn_small_word
import random_network_er
from numpy import *


def pre_kernel():
	a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	return a


def pre_conv(pre_conv_matrix, m):
	pre_conv_m = len(pre_conv_matrix)
	pre_conv_k = pre_conv_m - m + 1
	after_m = [([0] * pre_conv_k) for si in range(pre_conv_k)]
	kernel_a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	for pre_i in range(pre_conv_k):
		for pre_j in range(pre_conv_k):
			pre_temp = 0
			for i in range(m):
				for j in range(m):
					pre_temp += pre_conv_matrix[pre_i + i][pre_j + j] * kernel_a[i][j]
			if pre_temp > m - 1:
				after_m[pre_i][pre_j] = 1

	return after_m


def pre_pooling(pre_pooling_matrix, pre_pooling_mul=2):
	pre_pooling_m = len(pre_pooling_matrix)
	pre_pooling_k = pre_pooling_m / pre_pooling_mul
	after_m = [([0] * pre_pooling_k) for si in range(pre_pooling_k)]
	kernel_a = [[1.5, 1, 1.5], [1, 1, 1], [1.5, 1, 1.5]]
	for pre_i in range(0, pre_pooling_m, pre_pooling_mul):
		for pre_j in range(0, pre_pooling_m, pre_pooling_mul):
			pre_temp = 0
			for i in range(pre_pooling_mul):
				for j in range(pre_pooling_mul):
					pre_temp += pre_pooling_matrix[pre_i + i][pre_j + j] * kernel_a[i][j]
			if pre_temp > 1:
				after_m[pre_i/pre_pooling_mul][pre_j/pre_pooling_mul] = 1

	return after_m


def change_matrix(ch_matrix, aim_n=500):
	after_m = ch_matrix
	while len(after_m) >= 2 * aim_n:
		print "Image so big to pooling first"
		after_m = pre_pooling(after_m, 2)

	return after_m


if __name__ == '__main__':
	n = 800

	ba = ncn_small_word.small_word(n, 20, 0.3)
	# ba = random_network_er.random_network(n, 0.06)
	# ba = scale_free_ba.scale_free(n, 7, 4)

	ba = matrix_random(ba)
	a, b, c = average_feature(ba)
	print (a, c)

	imsave("demo.png", ba)
	# degree_distribution(ba)
	a, b, c = average_feature(ba)
	print (a, c)

	After_m = change_matrix(ba, 400)
	imsave("demo001.png", After_m)
	# degree_distribution(After_m)
	a, b, c = average_feature(After_m)
	print (a, c)

	ba = matrix_change(ba)
	degree_distribution(ba)
	a, b, c = average_feature(ba)
	print (a, c)

	After_m = change_matrix(ba, 400)
	degree_distribution(After_m)
	a, b, c = average_feature(After_m)
	print (a, c)
