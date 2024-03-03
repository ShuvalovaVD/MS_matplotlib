# Графики для Y: гистограмма, полигон, ПРВ для равномерного распределения
import numpy as np
from scipy.stats import norm  # доп установить модуль scipy: pip install scipy
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# набор данных для гистограммы
x_all_hist = [4.30, 8.48, 12.66, 16.84, 21.02, 25.20, 29.38, 33.56, 37.74, 41.92]  # те x, к-рые слева от столбиков
x_left_hist = 4.30  # самое левое значение
x_right_hist = 46.10  # самое правое значение
y_all_hist = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]
width_hist = 4.18  # ширина интервала
# набор данных для полигона
x_all_pol = [6.38, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all_pol = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]

# создание фигуры
fig = plt.figure(figsize=(15, 6))
p = fig.add_subplot()
# гистограмма
p.bar(x_all_hist, y_all_hist, width=width_hist, align="edge", color="orange", linewidth=1.0, edgecolor="black",
      label='гистограмма')
# полигон
p.plot(x_all_pol, y_all_pol, color="red", marker="o", label='полигон')

# ПРВ для равномерного распределения
a, b = 4.30, 46.10  # параметры a и b
f_val = round(1 / (b - a), 2)  # 1 / (b - a), округленное до 2-х знаков после точки
p.plot([a, b], [f_val, f_val], color="green", linewidth=2.0, marker="o", label="ПРВ для равномерного распределения")
# все равно придётся фотошопить, все непонятные числа подбирались, чтобы лучше отобразить график
p.plot([a - 3, a - 0.30], [0, 0], linewidth=4.0, color="green")
p.scatter([a], [0.0004], marker="o", linewidth=1.5, color="white", edgecolors="black", s=50)
p.plot([b + 0.38, b + 3], [0, 0], linewidth=4.0, color="green")
p.scatter([b], [0.0004], marker="o", linewidth=1.5, color="white", edgecolors="black", s=50)

# легенда
plt.title("Графики для Y: гистограмма, полигон, ПРВ для равномерного распределения")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
p.legend(loc='upper right')
# отметки
x_all_unique = list(set(x_all_hist + [x_right_hist] + x_all_pol))
y_all_unique = list(set(y_all_hist + y_all_pol))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
