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
import ncn_word
import random_network_er
import numpy as np


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
                after_m[pre_i / pre_pooling_mul][pre_j / pre_pooling_mul] = 1
    # As an undirected graph, the link matrix needs to do some minor processing.
    for i in range(pre_pooling_k):
        after_m[i][i] = 0
    for i in range(pre_pooling_k):
        for j in range(i + 1, pre_pooling_k):
            after_m[j][i] = after_m[i][j]
    return after_m


def change_matrix(ch_matrix, aim_n=500):
    after_m = ch_matrix
    while len(after_m) >= 2 * aim_n:
        # print "Image so big to pooling first"
        after_m = pre_pooling(after_m, 2)

    return after_m


def class_compress():
    """
    This part for class networks compress.
    :return:
    """
    n = 400  # original size of networks.
    ba = ncn_small_word.small_word(n, 30, 0.2)
    # ba = random_network_er.random_network(n, 0.06)
    # ba = scale_free_ba.scale_free(n, 7, 4)
    # ba = ncn_word.normal_word(n, 30)

    ba = matrix_random(ba)
    ba = matrix_change(ba)
    imsave("demo.png", ba)
    a, b, c = average_feature(ba)
    print (a, c)
    # degree_distribution(ba)

    after_m = change_matrix(ba, 200)
    imsave("demo001.png", after_m)
    # degree_distribution(after_m)
    a, b, c = average_feature(after_m)
    print (a, c)


def test_data(size=400, n=200):
    """
    load data for networks compress.
    :param size:
    :param n:
    :return:
    """
    y_label = np.array([0 for i in range(size)])
    x_image = np.zeros((size, 1, n, n))
    echo = int(size / 200)
    iter_num = 0
    print("start to make matrix>>>>>>")
    print("small_word>>>>>>>>>")
    for k in [5, 10, 15, 17, 20]:
        for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.75, 0.8]:
            for ii in range(echo):
                ws = ncn_small_word.small_word(2*n, k, p)
                ws = matrix_random(ws)
                ws = matrix_change(ws)
                ws = change_matrix(ws, n)
                y_label[iter_num] = 1
                x_image[iter_num, :, :, :] = ws
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("normal network>>>>>>>>>>")
    for num in [2, 3, 4, 5, 6]:
        for si in range(10):
            for ii in range(echo):
                nn = ncn_word.normal_word(2*n, num)
                nn = matrix_random(nn)
                nn = matrix_change(nn)
                nn = change_matrix(nn, n)
                y_label[iter_num] = 0
                x_image[iter_num, :, :, :] = nn
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("scale free network>>>>>>>>>")
    for num in [2, 3, 4, 5, 6]:
        for m in [2, 3, 5, 10, 15, 17, 20, 22, 25, 27]:
            for ii in range(echo):
                ba = scale_free_ba.scale_free(2*n, num, m)
                ba = matrix_random(ba)
                ba = matrix_change(ba)
                ba = change_matrix(ba, n)
                y_label[iter_num] = 3
                x_image[iter_num, :, :, :] = ba
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("random network>>>>>>>>>")
    for p in [0.1, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.23, 0.24, 0.25]:
        for si in range(5):
            for ii in range(echo):
                er = random_network_er.random_network(2*n, p)
                er = matrix_random(er)
                er = matrix_change(er)
                er = change_matrix(er, n)
                y_label[iter_num] = 2
                x_image[iter_num, :, :, :] = er
                iter_num += 1
    print("iter_num = " + str(iter_num))

    y_label = y_label.reshape((size,))
    x_image = x_image.reshape((size, 1, n, n))

    return x_image, y_label

if __name__ == '__main__':
    class_compress()
