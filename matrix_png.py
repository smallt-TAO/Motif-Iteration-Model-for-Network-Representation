"""
  This function for a matrix transfer to a picture.
  __author__ = 'Smalltao'
  """

from scipy.misc import imsave
import scale_free_ba
import ncn_small_word
import random_network_er
from kronecker_graphs import kronecker_graphs
from numpy import *
from algorithm import matrix_random
from algorithm import matrix_change

n = 768

print "*** Start the small word simulation ***"
for k in [5, 10, 20, 30]:
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        for ii in range(2):
            ws = ncn_small_word.small_word(n, k, p)
            ws = matrix_random(ws)
            ws = matrix_change(ws)
            imsave("G:\\code_Python\\see_network\\data_ws\\small_word_{0}_{1}_{2}.png".format(str(k), str(p), str(ii)),
                   ws)

print "*** Start the scale free simulation ***"
for num in [2, 3, 4, 5]:
    for m in [2, 3, 5, 10, 15, 20, 25, 30]:
        for ii in range(2):
            ba = scale_free_ba.scale_free(n, num, m)
            ba = matrix_random(ba)
            ba = matrix_change(ba)
            imsave(
                "G:\\code_Python\\see_network\\data_ba\\scale_free_{0}_{1}_{2}.png".format(str(num), str(m), str(ii)),
                ba)

print "*** Start the random network simulation ***"
for p in [0.1, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24]:
    for ii in range(8):
        er = random_network_er.random_network(n, p)
        er = matrix_random(er)
        er = matrix_change(er)
        imsave("G:\\code_Python\\see_network\\data_er\\random_{0}_{1}.png".format(str(p), str(ii)), er)

print "*** Start the kronecker graphs simulation ***"
matrix1 = [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
matrix2 = [[0, 1, 0], [1, 0, 1], [0, 1, 1]]
matrix3 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
matrix4 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
matrix5 = [[0, 1], [1, 1]]
matrix6 = [[1, 0], [0, 1]]

for k_g in [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6]:
    for i in range(4):
        kg = kronecker_graphs(k_g, n)
        kg = matrix_random(kg)
        kg = matrix_change(kg)
        imsave("G:\\code_Python\\see_network\\data_kg\\kronecker_{1}_{0}.png".format(i, str(k_g)), kg)
