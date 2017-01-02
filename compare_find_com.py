"""
__author__ = 'Smalltao'
This code for compare of diff find-communities.
"""

from networkx import read_gml
from scipy.misc import imsave

import networkx as nx
import community

from numpy import *
from algorithm01 import matrix_change
import matplotlib.pyplot as plt


def load_data():
    G = read_gml('G:\\code_Python\\see_network\\test_data\\karate.gml')
    load_dict = community.best_partition(G)
    load_m = 34
    load_matrix = [([0] * load_m) for _ in range(load_m)]
    load_list = G.edges()
    for i in range(G.number_of_edges()):
        load_matrix[load_list[i][0] - 1][load_list[i][1] - 1] = 1
        load_matrix[load_list[i][1] - 1][load_list[i][0] - 1] = 1
    return load_matrix, load_dict


def dict2array(dict0):
    dict_num = max(dict0.values()) + 1
    dict_array = [[] for _ in range(dict_num)]
    for k, v in dict0.iteritems():
        k -= 1
        dict_array[int(v)].append(k)
    return dict_array


def color_image(color_matrix, n=30, k=4):
    color_size = len(color_matrix)
    color_max = k
    color_iter = int(125.0 / color_max)
    color_matrix_b = [[[255, 255, 255] for _ in range(color_size)] for si in range(color_size)]
    for i in range(color_max):
        for iter_i in range(n):
            for iter_j in range(n):
                if color_matrix[iter_i][iter_j] == i and i != 0:
                    color_matrix_b[iter_i][iter_j] = [145, 0 + i * color_iter, 255 - i * color_iter]

    return color_matrix_b


def local_old(matrix0, list0):
    """
    :param matrix0:
    :param list0: for example [[1, 2, 3], [5, 8]]
    :return:
    """
    array0 = []  # rank again by the number of community
    for i in range(len(list0)):
        array0.extend(list0[i])

    num = len(matrix0)
    matrix_old = [([0] * num) for _ in range(num)]
    for i in range(num):
        for j in range(num):
            matrix_old[i][j] = matrix0[array0[i]][array0[j]]
    return matrix_old


def local_change(matrix, list):
    """
    :param matrix:
    :param list: for example [[1, 2, 3], [5, 8]]
    :return:
    """
    local_list = []  # rank the list
    array = []  # rank again by the number of community

    # rank the list
    for i in range(len(list)):
        load_len = len(list[i])
        array.append(load_len)
        matrix0 = [([0] * load_len) for _ in range(load_len)]
        for iter_i in range(load_len):
            for iter_j in range(load_len):
                matrix0[iter_i][iter_j] = matrix[list[i][iter_i]][list[i][iter_j]]
        matrix0, local_array = matrix_change(matrix0)
        for iter_i in range(load_len):
            local_list.append(list[i][local_array[iter_i]])

    # reconstruct the matrix
    num = len(matrix)
    matrix_new = [([0] * num) for _ in range(num)]
    for i in range(num):
        for j in range(num):
            matrix_new[i][j] = matrix[local_list[i]][local_list[j]]

    # mark the diff community
    local_iter = 0
    for ii in range(len(list)):
        load_len = len(list[ii])
        for iter_i in range(load_len):
            for iter_j in range(load_len):
                if matrix_new[iter_i + local_iter][iter_j + local_iter] != 0:
                    matrix_new[iter_i + local_iter][iter_j + local_iter] += ii
        local_iter += load_len

    return matrix_new


def plot_com():
    G = read_gml('G:\\code_Python\\see_network\\test_data\\karate.gml')
    partition0 = community.best_partition(G)

    # drawing
    size0 = float(len(set(partition0.values())))
    pos = nx.spring_layout(G)
    count = 0.
    for com in set(partition0.values()):
        count += 1.
        list_nodes = [nodes for nodes in partition0.keys() if partition0[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=str(count / size0))

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()


def main():
    matrix0, dict0 = load_data()
    array0 = dict2array(dict0)
    matrix_old = local_old(matrix0, array0)
    imsave('demo_old.png', matrix_old)

    matrix_new = local_change(matrix0, array0)
    imsave('demo_new.png', matrix_new)
    # print matrix_new

    # color the matrix
    matrix_color = color_image(matrix_new, n=len(matrix_new), k=5)
    imsave('demo_color.png', matrix_color)

    plot_com()


if __name__ == '__main__':
    main()

