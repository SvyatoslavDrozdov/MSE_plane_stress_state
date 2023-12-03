from config import length, height
from data_and_configuration.write_and_read_data import write_data
from stiffness.element_stiffness_1_and_2 import write_K_1_K_2

# В этом файле генерируются глобальные матрицы жесткости для элементов с разбиением на деления [N, 2*N].
# От N = N_1, до N = N_2: range(N_1, N_2+1)

for task in range(1, 2):
    height_number = task
    length_number = 2 * task
    write_K_1_K_2(length, height, length_number, height_number)
    write_data(length, height, length_number, height_number)
    print(f"Task {task} completed ----------------------------------\n")
