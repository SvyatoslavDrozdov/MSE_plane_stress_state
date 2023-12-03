import numpy as np
from data_and_configuration.config import E
from scipy import integrate
import time


def get_K_e(elem_coord):
    start_time = time.time()

    # elem_coord = [[x_0,y_0], ... , [x_5, y_5]]
    def f(x, y):
        return np.array([1, x, y, x ** 2, x * y, y ** 2])

    def df_dx(x, y):
        return np.array([0, 1, 0, 2 * x, y, 0])

    def df_dy(x, y):
        return np.array([0, 0, 1, 0, x, 2 * y])

    reversed_M = [f(elem_coord[i][0], elem_coord[i][1]) for i in range(6)]
    M = np.linalg.inv(reversed_M)

    def dN_dx(x, y):
        return np.dot(df_dx(x, y), M)

    def dN_dy(x, y):
        return np.dot(df_dy(x, y), M)

    def B(x, y):
        dN_dx_xy = dN_dx(x, y)
        dN_dy_xy = dN_dy(x, y)
        array = [
            [dN_dx_xy[0], 0, dN_dx_xy[1], 0, dN_dx_xy[2], 0, dN_dx_xy[3], 0, dN_dx_xy[4], 0, dN_dx_xy[5], 0],
            [0, dN_dy_xy[0], 0, dN_dy_xy[1], 0, dN_dy_xy[2], 0, dN_dy_xy[3], 0, dN_dy_xy[4], 0, dN_dy_xy[5]],
            [dN_dy_xy[0], dN_dx_xy[0], dN_dy_xy[1], dN_dx_xy[1], dN_dy_xy[2], dN_dx_xy[2], dN_dy_xy[3], dN_dx_xy[3],
             dN_dy_xy[4], dN_dx_xy[4], dN_dy_xy[5], dN_dx_xy[5], ]
        ]
        return np.array(array)

    def integrand_function(inner_i, inner_j):
        def func(y, x):
            value = np.dot(np.transpose(B(x, y)), E)
            value = np.dot(value, B(x, y))
            return value[inner_i][inner_j]

        return func

    # This returns "lower_type" if 3 points of element aare making its base, and "upper_type" in other case.
    if elem_coord[0][1] == elem_coord[1][1] == elem_coord[2][1]:
        element_type = "lower_type"
    else:
        element_type = "upper_type"

    if element_type == "lower_type":
        a = elem_coord[0][0]
        b = elem_coord[2][0]
    else:
        a = elem_coord[3][0]
        b = elem_coord[5][0]

    y_beginning = elem_coord[0][1]
    y_end = elem_coord[5][1]

    def y_line(x):
        return (y_end - y_beginning) / (b - a) * x + (b * y_beginning - a * y_end) / (b - a)

    def y_bottom(x):
        return y_beginning + 0 * x

    def y_top(x):
        return y_end + 0 * x

    K_e = np.zeros((12, 12))

    if element_type == "lower_type":
        for i in range(0, 12):
            for j in range(i, 12):
                K_e[i][j] = integrate.dblquad(integrand_function(i, j), a, b, y_bottom, y_line, epsabs=1e-3)[0]
    else:
        for i in range(0, 12):
            for j in range(i, 12):
                K_e[i][j] = integrate.dblquad(integrand_function(i, j), a, b, y_line, y_top, epsabs=1e-3)[0]
    for i in range(0, 12):
        for j in range(0, i):
            K_e[i][j] = K_e[j][i]

    end_time = time.time()
    print(f"The stiffness matrix was calculated in {round(end_time - start_time, 2)} seconds ")

    return K_e
