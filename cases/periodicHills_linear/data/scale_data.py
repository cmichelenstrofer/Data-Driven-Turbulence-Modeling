#!/usr/bin/env python3

import numpy as np

files = ['UxFullField', 'UyFullField', 'UzFullField']

nu_ratio = 0.00017857142857142857 / 5e-6

for file in files:
    np.savetxt(file, np.loadtxt(file) * nu_ratio)
