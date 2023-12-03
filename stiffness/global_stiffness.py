import numpy as np
from geometry.make_geometry import nodes_of_elements


def global_element_matrix(all_element_K, size):
    """
    :param all_element_K: {1: K_1, 2:K_2 ...} - список ключи которого это номера узлов с единицы, а значения которого -
        это матрицы жесткостей соответствующих элементов
    :param size: [количество делений по высоте, количество делений по длине]
    :return: global_K - глобальная матрица жесткости конструкции
    """
    height_number = int(size.split("_")[0])
    length_number = int(size.split("_")[1])
    number_of_nodes = (2 * length_number + 1) * (2 * height_number + 1)
    global_K = np.zeros((2 * number_of_nodes, 2 * number_of_nodes))

    all_nodes_of_element = nodes_of_elements(length_number, height_number)
    for element in all_element_K:
        K_e = all_element_K[element]
        nodes = all_nodes_of_element[element]

        def rearrangement(x):
            return nodes[x] - 1

        for i in range(6):
            for j in range(6):
                x_0_0_local = 2 * i
                y_0_0_local = 2 * j

                x_0_0_global = 2 * rearrangement(i)
                y_0_0_global = 2 * rearrangement(j)

                global_K[x_0_0_global][y_0_0_global] += K_e[x_0_0_local][y_0_0_local]
                global_K[x_0_0_global + 1][y_0_0_global] += K_e[x_0_0_local + 1][y_0_0_local]
                global_K[x_0_0_global][y_0_0_global + 1] += K_e[x_0_0_local][y_0_0_local + 1]
                global_K[x_0_0_global + 1][y_0_0_global + 1] += K_e[x_0_0_local + 1][y_0_0_local + 1]

    return global_K
