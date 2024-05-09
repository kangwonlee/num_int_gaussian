import random

import matplotlib.pyplot as plt
import numpy as np


import numerical_integration


def sample_main():
    x_begin = 0
    x_end_array = np.logspace(3, 6)

    n = random.randint(100, 150) * 2

    area_list = []

    for x_end in x_end_array:
        result_2 = numerical_integration.gauss_int_2(x_begin, x_end, n)

        area_list.append(result_2['area_2'])

    area_array = np.array(area_list)
    going_where = (area_array * 2) ** 2

    plt.semilogx(x_end_array, going_where)
    plt.xlabel('integration range end point')
    plt.ylabel('((Gaussisan integral) * 2) ** 2')
    plt.grid(True)
    plt.savefig('sample.png')


if "__main__" == __name__:
    sample_main()
