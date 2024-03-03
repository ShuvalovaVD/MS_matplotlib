# Графики для X: гистограмма, полигон, ПРВ для нормального распределения
import numpy as np
from scipy.stats import norm  # доп установить модуль scipy: pip install scipy
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# набор данных для гистограммы
x_all_hist = [1.99, 3.96, 5.93, 7.90, 9.87, 11.84, 13.81, 15.78, 17.75, 19.72]  # те x, к-рые слева от столбиков
x_left_hist = 1.99  # самое левое значение
x_right_hist = 21.69  # самое правое значение
y_all_hist = [0.04, 0.06, 0.10, 0.10, 0.05, 0.04, 0.03, 0.04, 0.03, 0.03]
width_hist = 1.97  # ширина интервала
# набор данных для полигона
x_all_pol = [2.98, 4.95, 6.92, 8.89, 10.86, 12.83, 14.80, 16.77, 18.74, 20.71]
y_all_pol = [0.04, 0.06, 0.10, 0.10, 0.05, 0.04, 0.03, 0.04, 0.03, 0.03]

# создание фигуры
fig = plt.figure(figsize=(15, 6))
p = fig.add_subplot()
# гистограмма
p.bar(x_all_hist, y_all_hist, width=width_hist, align="edge", color="orange", linewidth=1.0, edgecolor="black")
# полигон
p.plot(x_all_pol, y_all_pol, color="red", marker="o")

# ПРВ нормального распределения
step_norm = 0.001  # шаг
x_norm = np.arange(x_left_hist, x_right_hist, step_norm)
m = 10.10  # параметр матожидания
sd = 5.00  # параметр среднего квадратичного отклонения
f_max = round(0.3989 / sd, 2)  # максимальное значение ф-ции, округлённое до двух знаков после точки
p.plot(x_norm, norm.pdf(x_norm, m, sd), color="green")

# легенда
plt.title("Графики для X: гистограмма, полигон, ПРВ для нормального распределения")
plt.ylabel("n_i/(n*w)")
plt.xlabel("x")
# отметки
x_all_unique = list(set(x_all_hist + [x_right_hist] + x_all_pol))
y_all_unique = list(set(y_all_hist + y_all_pol + [f_max]))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
