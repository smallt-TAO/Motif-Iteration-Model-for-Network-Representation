# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Smalltao'
This demo code for the change of network replaced.

"""

from numpy import *
from algorithm import matrix_change
from feature_matrix import average_feature
from feature_matrix import degree_distribution


def pre_pooling(pre_pooling_matrix, pre_pooling_mul=2):
    pre_pooling_m = len(pre_pooling_matrix)
    pre_pooling_k = pre_pooling_m / pre_pooling_mul
    after_m = [([0] * pre_pooling_k) for si in range(pre_pooling_k)]
    kernel_a = [[1.5, 1], [1, 1]]
    for pre_i in range(0, pre_pooling_m, pre_pooling_mul):
        for pre_j in range(0, pre_pooling_m, pre_pooling_mul):
            pre_temp = 0
            for i in range(pre_pooling_mul):
                for j in range(pre_pooling_mul):
                    pre_temp += pre_pooling_matrix[pre_i + i][pre_j + j] * kernel_a[i][j]
            if pre_temp > 1:
                after_m[pre_i / pre_pooling_mul][pre_j / pre_pooling_mul] = 1
    # As an undirected graph, the link matrix needs to do some minor processing.
    for i in range(pre_pooling_k):
        after_m[i][i] = 0
    for i in range(pre_pooling_k):
        for j in range(i + 1, pre_pooling_k):
            after_m[j][i] = after_m[i][j]
    return after_m


def handle_data(st):
    num = 198  # origin size is 198
    matrix_data = [([0] * num) for si in range(num)]
    fr = open(st + ".txt")
    for eachLine in fr:
        line = eachLine.strip().split()
        (m, n) = (int(line[0]) - 1, int(line[1]) - 1)
        matrix_data[m][n] = 1
        matrix_data[n][m] = 1
    matrix_data = matrix_change(matrix_data)
    a, b, c = average_feature(matrix_data)
    print "average SP and average C of the real networks is"
    print (a, c)
    print

    # replaced the networks
    matrix_data0 = pre_pooling(matrix_data, 2)
    a, b, c = average_feature(matrix_data0)
    print "average SP and average C of the replaced real networks is"
    print (a, c)
    print
    degree_distribution(matrix_data, matrix_data0)


def handle_data0():
    st = "G:\\code_Python\\see_network\\test_data\\SmaGri"
    num = 1060  # origin size is 1059
    matrix_data = [([0] * num) for si in range(num)]
    fr = open(st + ".txt")
    for eachLine in fr:
        line = eachLine.strip().split()
        for j in range(1, len(line)):
            (m, n) = (int(line[0]) - 1, int(line[j]) - 1)
            matrix_data[m][n] = 1
            matrix_data[n][m] = 1
    matrix_data = matrix_change(matrix_data)
    a, b, c = average_feature(matrix_data)
    print "average SP and average C of the real networks is"
    print (a, c)

    # replaced the networks
    matrix_data0 = pre_pooling(matrix_data, 2)
    a, b, c = average_feature(matrix_data0)
    print "average SP and average C of the replaced real networks is"
    print (a, c)
    print
    degree_distribution(matrix_data, matrix_data0)


if __name__ == "__main__":
    handle_data("G:\\code_Python\\see_network\\test_data\\Jazz")
    handle_data0()
