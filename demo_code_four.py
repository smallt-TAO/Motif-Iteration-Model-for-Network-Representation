# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This demo for show the picture for paper.
__author__ = 'Smalltao'

"""
from scipy.misc import imsave

import scale_free_ba
import ncn_small_word
import random_network_er

from algorithm import matrix_random
from algorithm import matrix_change

n = 400


print "*** Start the small word simulation ***"

ws = ncn_small_word.small_word(n, 25, 0.2)
ws = matrix_random(ws)
imsave("G:\\code_Python\\see_network\\test_data\\SW1.eps", ws)
ws = matrix_change(ws)
imsave("G:\\code_Python\\see_network\\test_data\\SW2.eps", ws)

print "*** Start the scale free simulation ***"

ba = scale_free_ba.scale_free(n, 4, 5)
ba = matrix_random(ba)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_003.png", ba)
ba = matrix_change(ba)
imsave("G:\\code_Python\\see_network\\test_data\\small_word_004.png", ba)

print "*** Start the random network simulation ***"
er = random_network_er.random_network(n, 0.06)
er = matrix_random(er)
imsave("G:\\code_Python\\see_network\\test_data\\SW3.eps", er)
er = matrix_change(er)
imsave("G:\\code_Python\\see_network\\test_data\\SW4.eps", er)

print "*** Start the small word simulation ***"
for i in range(1, 10):
    p = 1.0 * i / 10
    ws = ncn_small_word.small_word(n, 25, p)
    ws = matrix_random(ws)
    ws = matrix_change(ws)
    imsave("G:\\code_Python\\see_network\\test_data\\demo_ws_{}.png".format(p), ws)


print "*** Start the scale free simulation ***"
for i in range(1, 10):
    p = 1.0 * i / 10
    ba = scale_free_ba.scale_free(n, 4, 25, key_p=p)
    ba = matrix_random(ba)
    ba = matrix_change(ba)
    imsave("G:\\code_Python\\see_network\\test_data\\demo_ba_{}.png".format(p), ba)
