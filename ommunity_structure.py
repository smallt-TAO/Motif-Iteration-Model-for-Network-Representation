# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用算法1进行更多的尝试。
"""

from scipy.misc import imsave
import scale_free_ba
import ncn_small_word
import random_network_er
from numpy import *
from algorithm01 import matrix_random
from algorithm01 import matrix_change
import random


def color_image(color_matrix):
    color_size = len(color_matrix)
    color_matrix_b = [[[0, 0, 0] for si in range(color_size)] for y in range(color_size)]
    for i in range(n):
        for j in range(n):
            if color_matrix[i][j] == 1:
                color_matrix_b[i][j] = [100, 80, 90]
            if color_matrix[i][j] == 2:
                color_matrix_b[i][j] = [200, 200, 30]
    return color_matrix_b


n = 30
ws = ncn_small_word.small_word(n, 2, 0.3)
ws, Array = matrix_random(ws)
ws, Array1 = matrix_change(ws)

# Array change with Array1
Array_new = []
for i in Array1:
    Array_new.append(Array[i])
print Array_new

ws1 = ncn_small_word.small_word(n, 2, 0.3)
ws1, Array1 = matrix_random(ws1)
ws1, Array11 = matrix_change(ws1)

# Array change with Array1
Array_new1 = [n] * n
start = 0
for i in Array1:
    Array_new1[start] += Array1[i]
    start += 1
print Array_new1

Array_new += Array_new1
print Array_new

matrix_b = [([0] * 2 * n) for si in range(2 * n)]
for i in range(n):
    for j in range(n):
        if ws[i][j] == 1:
            matrix_b[i][j] = 2
for i in range(n, 2 * n):
    for j in range(n, 2 * n):
        if ws1[i - n][j - n] == 1:
            matrix_b[i][j] = 4

imsave('demo.png', matrix_b)

matrix_b, Array111 = matrix_random(matrix_b)
matrix_b, Array111 = matrix_change(matrix_b)

imsave('demo001.png', matrix_b)
