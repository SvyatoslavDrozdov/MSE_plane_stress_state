from geometry.make_geometry import nodes_of_elements, create_geometry
from stiffness.optimized_element_stiffness import get_K_e


def write_data(length, height, length_number, height_number):
    """
    Эта функция создает текстовый файл с матрицами жесткости всех элементов.
    :param length: длина прямоугольной области
    :param height: высота прямоугольной области
    :param length_number: количество делений по длине
    :param height_number: количество делений по высоте
    :return: ничего не возвращает, но перезаписывает текстовый файл.
    """
    data = open(
        rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_storage\element_stiffness_{height_number}_{length_number}.txt",
        mode="w")

    nodes = nodes_of_elements(length_number, height_number)
    geometry = create_geometry(length, height, length_number, height_number)
    for element in nodes:
        element_nodes = sorted(nodes[element])
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


def read_data(size):
    """
    :param size: [количество делений по высоте, количество делений по длине]
    :return: {1: K_1, 2:K_2 ...} - список ключи которого это номера узлов с единицы, а значения которого -
        это матрицы жесткостей соответствующих элементов
    """
    data = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_storage\element_stiffness_{size}.txt")
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
