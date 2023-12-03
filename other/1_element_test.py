import numpy as np
import matplotlib.pyplot as plt
from data_and_configuration.write_and_read_data import read_data
from data_and_configuration.config import length, height

global_stiffness = read_data("2_4")
K_4 = global_stiffness[4]
Force = np.zeros(6)

# Force[0] = 1e10  # u of node:9
Force[1] = -1e10  # v of node:9
# Force[2] = -1e10  # u of node:16  -- ok
# Force[3] = +1e11 # v of node:16  -- ok
# Force[4] = +1e10  # u of node:17  -- ok
# Force[5] = -7e9  # v of node:17  -- ok

K_new = []
first_string = [K_4[4][4], K_4[4][5], K_4[4][8], K_4[4][9], K_4[4][10], K_4[4][11]]
second_string = [K_4[5][4], K_4[5][5], K_4[5][8], K_4[5][9], K_4[5][10], K_4[5][11]]
third_string = [K_4[8][4], K_4[8][5], K_4[8][8], K_4[8][9], K_4[8][10], K_4[8][11]]
fourth_string = [K_4[9][4], K_4[9][5], K_4[9][8], K_4[9][9], K_4[9][10], K_4[9][11]]
fifth_string = [K_4[10][4], K_4[10][5], K_4[10][8], K_4[10][9], K_4[10][10], K_4[10][11]]
sixth_string = [K_4[11][4], K_4[11][5], K_4[11][8], K_4[11][9], K_4[11][10], K_4[11][11]]

K_new.append(first_string)
K_new.append(second_string)
K_new.append(third_string)
K_new.append(fourth_string)
K_new.append(fifth_string)
K_new.append(sixth_string)
K_new = np.array(K_new)

solution_u = np.linalg.solve(K_new, Force)

print(solution_u)
displacement = np.zeros(12)
displacement[4] = solution_u[0]
displacement[5] = solution_u[1]
displacement[8] = solution_u[2]
displacement[9] = solution_u[3]
displacement[10] = solution_u[4]
displacement[11] = solution_u[5]
height = height / 2
length = length / 3
initial_position = [[0, 0], [0, height / 2], [length / 2, height / 2], [0, height], [length / 2, height],
                    [length, height]]
actual_position = []
for i in range(0, 6):
    old_x = initial_position[i][0]
    old_y = initial_position[i][1]
    new_x = old_x + displacement[2 * i]
    new_y = old_y + displacement[2 * i + 1]
    actual_position.append([new_x, new_y])

old_X = [initial_position[i][0] for i in range(6)]
old_Y = [initial_position[i][1] for i in range(6)]
old_X_to_plot = [old_X[0], old_X[1], old_X[3], old_X[4], old_X[5], old_X[2], old_X[0]]
old_Y_to_plot = [old_Y[0], old_Y[1], old_Y[3], old_Y[4], old_Y[5], old_Y[2], old_Y[0]]

new_X = [actual_position[i][0] for i in range(6)]
new_Y = [actual_position[i][1] for i in range(6)]
new_X_to_plot = [new_X[0], new_X[1], new_X[3], new_X[4], new_X[5], new_X[2], new_X[0]]
new_Y_to_plot = [new_Y[0], new_Y[1], new_Y[3], new_Y[4], new_Y[5], new_Y[2], new_Y[0]]
plt.axes().set_aspect('equal')
plt.plot(old_X_to_plot, old_Y_to_plot, marker="o", label="initial position")
plt.plot(new_X_to_plot, new_Y_to_plot, marker="o", label="actual position")

plt.grid()
plt.legend()
plt.show()
