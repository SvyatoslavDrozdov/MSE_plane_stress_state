import matplotlib.pyplot as plt

time = [0.0, 0.01, 0.03, 0.05, 0.09, 0.14, 0.61, 2.61, 7.81, 18.74, 39.32, 77.39, 182.45, 435.4, 725.48]
number_of_nodes = [15, 45, 91, 153, 231, 325, 861, 1891, 3321, 5151, 7381, 10011, 13041, 16471, 20301]

plt.plot(number_of_nodes, time, marker="o", color="blue")
plt.xlabel("Количество узлов")
plt.ylabel("Время расчета, сек")
plt.grid()
plt.show()
