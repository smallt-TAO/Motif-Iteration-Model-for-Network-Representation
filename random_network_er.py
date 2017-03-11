# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

__author__ = 'Smalltao'


def random_network(size, p):
    # init ncn
    matrix_b = [([0] * size) for si in range(size)]
    for i in range(size):
        for j in range(i, size):
            if random.random() < p:
                matrix_b[i][j] = 1
                matrix_b[j][i] = 1

    return matrix_b
