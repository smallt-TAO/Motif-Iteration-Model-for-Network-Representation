# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

__author__ = 'Smalltao'


def small_word(size, k, p):
    """
    :param size: size of the matrix
    :param k: size of the link limit
    :param p: size of the possibly
    :return: a small word network
    """
    # init ncn
    matrix_b = [([0] * size) for si in range(size)]
    for i in range(size):
        for j in range(i + 1, i + k / 2 + 1):
            if j < size:
                matrix_b[i][j] = 1
                matrix_b[j][i] = 1
            else:
                matrix_b[i][j - size] = 1
                matrix_b[j - size][i] = 1
    # create the small word
    for i in range(size):
        for j in range(i + 1, size):
            if matrix_b[i][j] != 0:
                if random.random() < p:
                    matrix_b[i][j] = 0
                    matrix_b[j][i] = 0
                    s = random.randint(i + 1, size - 1)
                    matrix_b[i][s] = 1
                    matrix_b[s][i] = 1

    return matrix_b
