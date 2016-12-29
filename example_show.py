# -*- coding: utf-8 -*-
"""
__author__ = 'Smalltao'
This demo for compare of change before and after.
"""

from scipy.misc import imsave

import scale_free_ba
import ncn_small_word
import random_network_er

from algorithm import matrix_random
from algorithm import matrix_change

n = 768


print "*** Start the small word simulation ***"

ws = ncn_small_word.small_word(n, 10, 0.2)
ws = matrix_random(ws)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_001.png", ws)
ws = matrix_change(ws)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_002.png", ws)

print "*** Start the scale free simulation ***"

ba = scale_free_ba.scale_free(n, 4, 5)
ba = matrix_random(ba)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_003.png", ba)
ba = matrix_change(ba)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_004.png", ba)

print "*** Start the random network simulation ***"
er = random_network_er.random_network(n, 0.12)
er = matrix_random(er)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_005.png", er)
er = matrix_change(er)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_006.png", er)
