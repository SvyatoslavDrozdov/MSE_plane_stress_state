from config import length, height
from write_and_read_data import write_data
from stiffness.element_stiffness_1_and_2 import write_K_1_K_2

for task in range(55, 56):
    height_number = task
    length_number = 2 * task
    write_K_1_K_2(length, height, length_number, height_number)
    write_data(length, height, length_number, height_number)
    print(f"Task {task} completed ----------------------------------\n")