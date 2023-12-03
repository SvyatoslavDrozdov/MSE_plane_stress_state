from solver.solve import get_solution
import time

start_time = time.time()


def write_convergence_data(data):
    """
    Эта функция записывает данные для построения графиков сходимости. Параметр point_position в начале отвечает за то
    перемещения какой точки будут отслеживаться: верхне правой ("top") или нижней правой ("bottom").
    :param data: "N_2*N" - разбиение на деления прямоугольной области.
    :return: ничего не возвращает, но перезаписывает текстовые файлы.
    """
    point_position = "bottom"

    if point_position == "top":
        info = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_and_configuration\convergence_analysis_top_right.txt",
                    mode="a")
    else:
        info = open(
            rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_and_configuration\convergence_analysis_bottom_right.txt",
            mode="a")

    for partition in data:
        start_iteration = time.time()

        height_number = int(partition.split("_")[0])
        length_number = int(partition.split("_")[1])
        number_of_elements = (2 * height_number + 1) * (2 * length_number + 1)
        displacement = get_solution(partition)

        if point_position == "top":
            last_u = displacement[-2]
            last_v = displacement[-1]
        else:
            last_u = displacement[2 * (2 * length_number + 1) - 2]
            last_v = displacement[2 * (2 * length_number + 1) - 1]

        info.write(f"{number_of_elements}, {last_u}, {last_v} \n")

        end_iteration = time.time()
        print(f"Задача была выполнена за {round(end_iteration - start_iteration, 2)} секунд. ")
    info.write(f"------------------------------------------------\n")
    end_time = time.time()
    print(f"Расчет занял {round(end_time - start_time, 2)} секунд")

    info.close()


geometry_partition_1 = ["1_2", "2_4", "3_6", "4_8", "5_10", "6_12", "10_20"]
geometry_partition_2 = ["15_30", "20_40", "25_50", "30_60"]
geometry_partition_3 = ["35_70"]
geometry_partition_4 = ["40_80"]
geometry_partition_5 = ["45_90"]
geometry_partition_6 = ["50_100"]

write_convergence_data(geometry_partition_1)
write_convergence_data(geometry_partition_2)
# write_convergence_data(geometry_partition_3)
# write_convergence_data(geometry_partition_4)
# write_convergence_data(geometry_partition_5)
# write_convergence_data(geometry_partition_6)
