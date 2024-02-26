# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:01:16 2024

@author: jonas
"""

import matplotlib.pyplot as plt
import numpy as np

h = np.loadtxt("data/a1.txt", dtype=float)
t = np.loadtxt("data/a2.txt", dtype=float)

V = 0.0002
g = 9.81
rho = 997.818

Q = V/t
p = h*rho*g

fig,ax=plt.subplots()
ax.plot(p, Q, "o")
ax.set_xlabel("\u0394p / Pa")
ax.set_ylabel("Qv / 10-\u2076 m\u00b3 s-\u00b9")

plt.legend()
plt.show()