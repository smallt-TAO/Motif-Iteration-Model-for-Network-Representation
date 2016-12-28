"""
  This function for a matrix transfer to a picture.
  __author__ = 'Smalltao'
  """
from __future__ import print_function
import scale_free_ba
import ncn_small_word
import random_network_er

import numpy as np
from algorithm import matrix_random
from algorithm import matrix_change


def find_matrix(size=300, n=200):
    y_label = np.array([0 for i in range(size)])
    x_image = np.zeros((size, 1, n, n))
    echo = int(size / 150)
    iter_num = 0
    print("start to make matrix>>>>>>")
    print("small_word>>>>>>>>>")
    for k in [5, 10, 15, 17, 20]:
        for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.75, 0.8]:
            for ii in range(echo):
                ws = ncn_small_word.small_word(n, k, p)
                ws = matrix_random(ws)
                ws = matrix_change(ws)
                y_label[iter_num] = 0
                x_image[iter_num, :, :, :] = ws
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("scale free network")
    for num in [2, 3, 4, 5, 6]:
        for m in [2, 3, 5, 10, 15, 17, 20, 22, 25, 27]:
            for ii in range(echo):
                ba = scale_free_ba.scale_free(n, num, m)
                ba = matrix_random(ba)
                ba = matrix_change(ba)
                y_label[iter_num] = 1
                x_image[iter_num, :, :, :] = ba
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("random network>>>>>>>>>")
    for p in [0.1, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.23, 0.24, 0.25]:
        for si in range(5):
            for ii in range(echo):
                er = random_network_er.random_network(n, p)
                er = matrix_random(er)
                er = matrix_change(er)
                y_label[iter_num] = 2
                x_image[iter_num, :, :, :] = er
                iter_num += 1
    print("iter_num = " + str(iter_num))

    y_label = y_label.reshape((size,))
    x_image = x_image.reshape((size, 1, n, n))

    return x_image, y_label
