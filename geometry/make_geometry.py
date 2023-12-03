def create_geometry(length, height, length_number, height_number):
    d = length / (2 * length_number)
    h = height / (2 * height_number)
    x_0 = [d * k for k in range(2 * length_number + 1)]
    y_0 = [h * k for k in range(2 * height_number + 1)]
    coord = []
    for j in range(2 * height_number + 1):
        for i in range(2 * length_number + 1):
            coord.append([x_0[i], y_0[j]])
    nodes = {}
    node_number = (2 * length_number + 1) * (2 * height_number + 1)
    for i in range(0, node_number):
        nodes.update({i + 1: coord[i]})
    return nodes  # Номер узла - координата


def nodes_of_elements(length_number, height_number):
    n_x = 2 * length_number + 1
    n_y = 2 * height_number + 1

    element_nodes = {}
    lvl = 1
    number = 0
    for position in range(1, length_number + 1):
        element_nodes.update(
            {position: sorted([1 + n_x * (lvl - 1) + 2 * (position - 1), 2 + n_x * (lvl - 1) + 2 * (position - 1),
                               3 + n_x * (lvl - 1) + 2 * (position - 1), n_x * lvl + 2 * position,
                               1 + n_x * lvl + 2 * position, 1 + n_x * (lvl + 1) + 2 * position])})
        number += 1
    k = 1
    while 2 * k + 1 < n_y:
        lvl = 2 * k + 1
        for position in range(1, length_number + 1):
            element_nodes.update(
                {number + 1: sorted([1 + n_x * (lvl - 1) + 2 * (position - 1), 2 + n_x * (lvl - 1) + 2 * (position - 1),
                                     3 + n_x * (lvl - 1) + 2 * (position - 1), 1 + n_x * (lvl - 2) + 2 * (position - 1),
                                     2 + n_x * (lvl - 2) + 2 * (position - 1),
                                     1 + n_x * (lvl - 3) + 2 * (position - 1)])})
            number += 1
        for position in range(1, length_number + 1):
            element_nodes.update(
                {number + 1: sorted([1 + n_x * (lvl - 1) + 2 * (position - 1), 2 + n_x * (lvl - 1) + 2 * (position - 1),
                                     3 + n_x * (lvl - 1) + 2 * (position - 1), n_x * lvl + 2 * position,
                                     1 + n_x * lvl + 2 * position, 1 + n_x * (lvl + 1) + 2 * position])})
            number += 1
        k += 1
    lvl = n_y
    for position in range(1, length_number + 1):
        element_nodes.update(
            {number + 1: sorted([1 + n_x * (lvl - 1) + 2 * (position - 1), 2 + n_x * (lvl - 1) + 2 * (position - 1),
                                 3 + n_x * (lvl - 1) + 2 * (position - 1), 1 + n_x * (lvl - 2) + 2 * (position - 1),
                                 2 + n_x * (lvl - 2) + 2 * (position - 1), 1 + n_x * (lvl - 3) + 2 * (position - 1)])})
        number += 1
    return element_nodes  # Номер элемента - список узлов принадлежащих элементу
