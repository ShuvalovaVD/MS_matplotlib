# Графики для Y: гистограмма, полигон, плотность распределения вероятности (ПРВ) для равномерного распределения
import numpy as np
from scipy.stats import norm  # доп установить модуль scipy: pip install scipy
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# набор данных для гистограммы
x_all_hist = [4.30, 8.48, 12.66, 16.84, 21.02, 25.20, 29.38, 33.56, 37.74, 41.92]  # коорд x, к-рые слева от столбиков
x_right_hist = 46.10  # тот x, к-рый идёт после всех столбиков
y_all_hist = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]  # знач столбиков по y, соответствуют x_all
width_hist = x_all_hist[1] - x_all_hist[0]  # ширина интервала
# набор данных для полигона
x_all_pol = [6.38, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all_pol = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]

# создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график, на к-ром несколько линий)
fig = plt.figure(figsize=(15, 6))
p = fig.add_subplot()
# гистограмма
p.bar(x_all_hist, y_all_hist, width=width_hist, align="edge", color="orange", linewidth=1.0, edgecolor="black",
      label='гистограмма')
# полигон (линейный график)
p.plot(x_all_pol, y_all_pol, color="red", marker="o", label='полигон')

# ПРВ равномерного распределения
a, b = 4.30, 46.10  # параметры a и b
f_val = round(1 / (b - a), 2)  # 1 / (b - a), округленное до 2-х знаков после точки
p.plot([a, b], [f_val, f_val], color="green", linewidth=2.0, marker="o", label="ПРВ равномерного распределения")
# продлеваем линии на l1 единиц слева и справа от границ гистограммы
l1 = 3
p.plot([a - l1, a], [0, 0], linewidth=4.0, color="green", marker="o", markerfacecolor="white", markersize=7)
p.plot([b, b + l1], [0, 0], linewidth=4.0, color="green", marker="o", markerfacecolor="white", markersize=7)
# теперь устанавливаем границы графика на l2 (l2 < l1) единиц слева и справа от границ гистограммы, чтобы обрезать линии
l2 = l1 - 1
plt.xlim(x_all_hist[0] - l2, x_right_hist + l2)

# легенда
plt.title("Графики для Y: гистограмма, полигон, ПРВ для равномерного распределения")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
p.legend(loc='upper right')
# отметки на осях (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике => множество set)
x_all_unique = list(set(x_all_hist + [x_right_hist] + x_all_pol))
y_all_unique = list(set(y_all_hist + y_all_pol + [f_val]))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
