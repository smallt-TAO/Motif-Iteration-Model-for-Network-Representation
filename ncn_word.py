# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Smalltao'


def normal_word(size, k):
    """
    :param size: size of the matrix
    :param k: size of the link limit
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

    return matrix_b

