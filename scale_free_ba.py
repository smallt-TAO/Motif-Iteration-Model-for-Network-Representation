# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

__author__ = 'Smalltao'


def scale_free(size, num, m, key_p=0):
    """
    :param size: size of the matrix.
    :param num: size of the matrix begin.
    :param m: size of limit.
    :return: matrix_b
    """
    # init the matrix
    matrix_b = [([0] * size) for si in range(size)]
    for i in range(num):
        for j in range(i):
            matrix_b[i][j] = 1
            matrix_b[j][i] = 1
    # init the degree of vector.
    degree_b = [0] * size
    for i in range(num):
        degree_b[i] = num - 1
    # add the vector
    for i in range(num, size):
        mm = 0
        dd = degree_b[:i]
        while mm < m:
            mm += 1
            degree_n = 0
            for j in range(i):
                degree_n += dd[j]
            p = [0] * i
            p[0] = dd[0] / (degree_n + 0.000001)
            for j in range(1, i):
                p[j] = p[j - 1] + dd[j] / (degree_n + 0.000001)
            for j in range(i):
                if random.random() < p[j]:
                    if random.random() > key_p:
                        matrix_b[i][j] = 1
                        matrix_b[j][i] = 1
                        degree_b[i] += 1
                        degree_b[j] += 1
                        dd[j] = 0
                        break
    return matrix_b
