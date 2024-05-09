import random

import numerical_integration


def sample_main():
    x_begin = 0
    x_end = 1000

    n = random.randint(100, 300)

    result_2 = numerical_integration.gauss_int_2(x_begin, x_end, n)

    a_array_2 = result_2['a_array_2']
    i = random.randint(0, len(a_array_2)-1)
    area_parabola_i = a_array_2[i]

    print(f"area of parabola #{i} is {area_parabola_i}")


if "__main__" == __name__:
    sample_main()
