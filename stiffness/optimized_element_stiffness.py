from stiffness.element_stiffness_1_and_2 import read_K_1_K_2


def get_K_e(elem_coord):
    K_1_2 = read_K_1_K_2()
    if elem_coord[0][1] == elem_coord[1][1] == elem_coord[2][1]:
        K_e = K_1_2[1]
    else:
        K_e = K_1_2[2]
    return K_e


# coord = [[0, 0], [3, 0], [6, 0], [3, 2], [6, 2], [6, 4]]
# print(get_K_e(coord))
