# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code for the feature of the network.
"""
import networkx as nx
import matplotlib.pyplot as plt


def degree_distribution(matrix, matrix0):
    degree_m = len(matrix)
    G = nx.Graph()
    for i in range(degree_m):
        for j in range(degree_m):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    degree = nx.degree_histogram(G)  # return all point degree distribution seq
    degree_x = range(len(degree))
    degree_y = [z / float(sum(degree)) for z in degree]  # Convert frequency to frequency
    degree_m0 = len(matrix0)
    G0 = nx.Graph()
    for i in range(degree_m0):
        for j in range(degree_m0):
            if matrix0[i][j] == 1:
                G0.add_edge(i, j)
    degree0 = nx.degree_histogram(G0)  # return all point degree distribution seq
    degree_x0 = range(len(degree0))
    degree_y0 = [z / float(sum(degree0)) for z in degree0]  # Convert frequency to frequency
    plt.loglog(degree_x, degree_y, color="red", linewidth=2)  # Institutional distribution curve
    plt.loglog(degree_x0, degree_y0, color="blue", linewidth=2)  # Institutional distribution curve
    plt.xlabel("Degree")
    plt.ylabel("Degree distribution")
    plt.show()


def average_feature(matrix):
    degree_m = len(matrix)
    G = nx.Graph()
    for i in range(degree_m):
        for j in range(degree_m):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    return nx.average_shortest_path_length(G), nx.betweenness_centrality(G), nx.average_clustering(G)
