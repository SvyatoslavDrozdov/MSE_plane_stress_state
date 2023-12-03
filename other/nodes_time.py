import matplotlib.pyplot as plt
import numpy as np

time = [0.0, 0.01, 0.03, 0.05, 0.09, 0.14, 0.61, 2.61, 7.81, 18.74, 39.32, 77.39, 182.45, 435.4, 725.48]
number_of_nodes = [15, 45, 91, 153, 231, 325, 861, 1891, 3321, 5151, 7381, 10011, 13041, 16471, 20301]

# a = 0.00000000007243220
# b = 0.00000043705351127
# c = - 0.00255430272907908
# d = 1.895058459
#
# X = np.array(number_of_nodes)
# Y = a * X ** 3 + b * X ** 2 + c * X + d
#
# plt.plot(X, Y, label="аппроксимация", marker="o", color="black")

# print(f"Для расчета 50_100 требуется {A * (np.exp(k * 20301) - 1) / 60} минут")
# print(f"Для расчета 55_110 требуется {A * (np.exp(k * 24531) - 1) / 60} минут")

# plt.plot(number_of_nodes, time, marker="o", label="Экспериментальные данные", color="blue")
plt.plot(number_of_nodes, time, marker="o", color="blue")
plt.xlabel("Количество узлов")
plt.ylabel("Время расчета, сек")
# plt.legend()
plt.grid()
plt.show()
