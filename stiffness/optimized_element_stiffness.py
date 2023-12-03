from stiffness.element_stiffness_1_and_2 import read_K_1_K_2


def get_K_e(elem_coord):
    """
    :param elem_coord: [[x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4], [x_5, y_5], [x_6, y_6]] - координаты узлов элемента
    :return: K_e - матрица жесткости элемента
    """
    K_1_2 = read_K_1_K_2()
    if elem_coord[0][1] == elem_coord[1][1] == elem_coord[2][1]:
        K_e = K_1_2[1]
    else:
        K_e = K_1_2[2]
    return K_e
