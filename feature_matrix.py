"""
This code for the matrix feature.
"""
import networkx as nx
import matplotlib.pyplot as plt


def degree_distribution(matrix):
    degree_m = len(matrix)
    G = nx.Graph()
    for i in range(degree_m):
        for j in range(degree_m):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    degree = nx.degree_histogram(G)  # return all point degree distribution seq
    degree_x = range(len(degree))
    degree_y = [z / float(sum(degree)) for z in degree]  # Convert frequency to frequency
    plt.loglog(degree_x, degree_y, color="blue", linewidth=2)  # Institutional distribution curve
    plt.show()


def average_feature(matrix):
    degree_m = len(matrix)
    G = nx.Graph()
    for i in range(degree_m):
        for j in range(degree_m):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    return nx.average_shortest_path_length(G), nx.betweenness_centrality(G), nx.average_clustering(G)
