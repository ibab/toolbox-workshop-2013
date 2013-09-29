# encoding: utf-8

from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
for n in range(1, 11):
    plt.plot(x, x**n)
    plt.title('$x^{{{}}}$'.format(n))
    plt.savefig('x_{}.pdf'.format(n))
    plt.clf()
