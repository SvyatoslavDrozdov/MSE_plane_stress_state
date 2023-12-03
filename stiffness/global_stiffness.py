import numpy as np
from geometry.make_geometry import nodes_of_elements
from data_and_configuration.write_and_read_data import read_data


def global_element_matrix(all_element_K, size):
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

# all_stiffness = read_data("8_8")
# K = global_element_matrix(all_stiffness, "8_8")
# print(K[1])
