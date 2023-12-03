import matplotlib.pyplot as plt
from data_and_configuration.config import length, height
from geometry.make_geometry import create_geometry, nodes_of_elements
from solver.solve import get_solution

# Этот код строит деформированное состояние. В нем в начале задается параметр "size".
# size: [количество делений по высоте, количество делений по длине]

size = "30_60"

displacement = get_solution(size)
height_number = int(size.split("_")[0])
length_number = int(size.split("_")[1])

element_number = 2 * length_number * height_number
nodes_number = (2 * length_number + 1) * (2 * height_number + 1)

initial_position = []
node_coord = create_geometry(length, height, length_number, height_number)
for node in range(1, nodes_number + 1):
    initial_position.append(node_coord[node])

actual_position = []
for i in range(0, nodes_number):
    old_x = initial_position[i][0]
    old_y = initial_position[i][1]
    new_x = old_x + displacement[2 * i]
    new_y = old_y + displacement[2 * i + 1]
    actual_position.append([new_x, new_y])

nodes = nodes_of_elements(length_number, height_number)

threes = True
counter = 0
for elements in range(0, element_number):
    node = sorted(nodes[elements + 1])
    if threes:
        forth = node[3]
        fifth = node[4]
        sixth = node[5]
        node[3] = fifth
        node[4] = sixth
        node[5] = forth
        node.append(node[0])

    else:
        third = node[2]
        node[2] = node[3]
        node[3] = node[4]
        node[4] = node[5]
        node[5] = third
        node.append(node[0])
    old_x_elem = []
    old_y_elem = []
    new_x_elem = []
    new_y_elem = []
    for i in range(0, 6 + 1):
        node_number_i = node[i]
        old_x_elem.append(initial_position[node_number_i - 1][0])
        old_y_elem.append(initial_position[node_number_i - 1][1])

        new_x_elem.append(actual_position[node_number_i - 1][0])
        new_y_elem.append(actual_position[node_number_i - 1][1])

    # plt.plot(old_x_elem, old_y_elem, marker="o", color="blue")
    # plt.plot(new_x_elem, new_y_elem, marker="o", color="red")

    plt.plot(old_x_elem, old_y_elem, color="blue")
    plt.plot(new_x_elem, new_y_elem, color="red")

    counter += 1
    if counter == length_number:
        counter = 0
        threes = not threes
plt.grid()
plt.show()
