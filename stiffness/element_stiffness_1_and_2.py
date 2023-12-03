from geometry.make_geometry import nodes_of_elements, create_geometry
from other.element_stiffness import get_K_e


def write_K_1_K_2(length, height, length_number, height_number):
    data = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\stiffness\element_stiffness_1_and_2.txt", mode="w")

    element_1 = 1
    element_2 = length_number + 1
    elements = [element_1, element_2]

    nodes = nodes_of_elements(length_number, height_number)
    geometry = create_geometry(length, height, length_number, height_number)

    for element in elements:
        element_nodes = nodes[element]
        coord = []
        for node in element_nodes:
            coord.append(geometry[node])
        stiffness = get_K_e(coord)
        data.write("\n")
        data.write(f"Element number {element}{150 * "-"}\n")
        for strings in stiffness:
            data.write(str(strings))
        data.write("\n")
    data.close()


def read_K_1_K_2():
    data = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\stiffness\element_stiffness_1_and_2.txt")
    text = ""
    for strings in data:
        if strings == "\n":
            pass
        if strings[0] == "E":
            text += "N"
        else:
            text += strings.replace("\n", "")

    stiffness = []
    elem = -1
    value = ""
    str_num = -1
    for letters in text:
        if letters == "N":
            stiffness.append([])
            str_num = -1
            elem += 1
            pass
        if letters == "[":
            stiffness[elem].append([])
            str_num += 1
        elif letters == "]":
            pass
        numbers_10 = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        if letters == " " or letters == "]":
            if value:
                number_to_add = float(value)
                stiffness[elem][str_num].append(number_to_add)
                value = ""
        if letters in numbers_10 or letters == "." or letters == "e" or letters == "+" or letters == "-":
            value += letters

    data.close()

    stiffness_data = {}
    for el in range(len(stiffness)):
        stiffness_data.update({el + 1: stiffness[el]})

    return stiffness_data
