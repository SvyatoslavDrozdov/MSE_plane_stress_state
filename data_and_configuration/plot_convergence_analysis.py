import matplotlib.pyplot as plt
import numpy as np


def read_data():
    """
    Эта функция читает рассчитанные заранее данные сходимости перемещений и выдает их в готовом для построения графика
    сходимости виде.
    :return: data_to_plot
    """
    # info = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_and_configuration\convergence_analysis_bottom_right.txt")
    info = open(rf"C:\Users\xxl20\PycharmProjects\FEM_2\data_and_configuration\convergence_analysis_top_right.txt")
    text = ""
    for strings in info:
        if strings == "------------------------------------------------\n":
            pass
        else:
            text += strings.replace("\n", ", ")
    data = text.split(", ")
    data = data[:len(data) - 1]
    data_to_plot = []

    for text_numbers in data:
        data_to_plot.append(float(text_numbers))

    data_to_plot_len = int(len(data_to_plot) / 3)
    data_to_plot = np.array(data_to_plot).reshape(data_to_plot_len, 3)

    return data_to_plot


elements_amount = []
last_U = []
last_V = []

calculated_cases = read_data()
for numbers in calculated_cases:
    elements_amount.append(numbers[0])
    last_U.append(numbers[1])
    last_V.append(numbers[2])

plt.plot(elements_amount, last_V, label="$v(n)$", marker="o")
plt.xlabel("Количество элементов")
plt.ylabel("Вертикальное перемещение, [м]")
plt.legend()
plt.grid()
plt.show()

plt.plot(elements_amount, last_U, label="$u(n)$", marker="o")
plt.xlabel("Количество элементов")
plt.ylabel("Горизонтальное перемещение, [м]")
plt.legend()
plt.grid()
plt.show()
