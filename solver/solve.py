import numpy as np
from data_and_configuration.write_and_read_data import read_data
from stiffness.global_stiffness import global_element_matrix


def get_solution(size):
    """
    :param size: [количество делений по высоте, количество делений по длине]
    :return: перемещения всех узлов: [u_1, v_1, u_2, v_2, ..., u_last, v_last]
    """
    height_number = int(size.split("_")[0])
    length_number = int(size.split("_")[1])
    nodes_number = (2 * length_number + 1) * (2 * height_number + 1)

    # Задание силы.
    force = np.zeros(2 * nodes_number - 2 * (2 * height_number + 1))
    # force[-1] = -1e8
    # force[-3] = -1e8
    # force[-5] = -1e8

    force[-1] = 3e9
    force[-3] = 3e9
    force[-5] = 3e9
    force[33] = -1e10
    force[35] = -1e10
    force[37] = -1e10
    global_stiffness = read_data(size)
    K = global_element_matrix(global_stiffness, size)

    equation_to_delete = []
    k = 0
    while 2 * (2 * length_number + 1) * k < 2 * nodes_number:
        equation_to_delete.append(2 * (2 * length_number + 1) * k)
        equation_to_delete.append(2 * (2 * length_number + 1) * k + 1)
        k += 1
    equation_to_delete = set(equation_to_delete)

    new_K = []
    for i in range(2 * nodes_number):
        add_line = []
        if i not in equation_to_delete:
            for j in range(2 * nodes_number):
                if j not in equation_to_delete:
                    add_line.append(K[i][j])
            new_K.append(add_line)
    new_K = np.array(new_K)

    calculated_u = np.linalg.solve(new_K, force)

    displacement = np.zeros(2 * nodes_number)
    calculated_u_num = 0
    for num in range(2 * nodes_number):
        if num not in equation_to_delete:
            displacement[num] = calculated_u[calculated_u_num]
            calculated_u_num += 1

    return displacement
