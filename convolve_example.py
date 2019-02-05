#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:00:44 2019

@author: efb
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

p = np.poly1d([1, .5, 4, 10])

x = np.arange(-10, 10, .5)

plt.plot(x, p(x))
plt.grid(True)
plt.show()


a = np.arange(0, 1, 0.005)
b = np.arange(1, 0, -0.005)
c = np.concatenate((a,b))

d = np.random.standard_normal(5000)

e = np.zeros(5000)
e[1000:1400] = c * .5
f = d + e

g = np.convolve(f, c, 'same')

plt.figure()
plt.plot(e)
plt.grid(True)
plt.show()

plt.figure()
plt.plot(f, '+')
plt.plot(e, '-r')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(f, '+')
plt.plot(g/10., '-y')
plt.plot(e, '-r')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(e, '+')
plt.plot(f, '+')
plt.grid(True)
plt.show()
