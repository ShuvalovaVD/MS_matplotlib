# ВАЖНО: код писала Таня, в моей РГР не было такого распределения
# Графики для X: гистограмма, полигон, ПРВ для экспоненциального распределения
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# набор данных для гистограммы
x_all_hist = [4.20, 14.89, 25.58, 36.26, 46.95, 57.64, 68.33, 79.01]  # те x, к-рые слева от столбиков
x_left_hist = 4.20  # самое левое значение
x_right_hist = 89.70  # самое правое значение
y_all_hist = [0.033, 0.023, 0.012, 0.010, 0.005, 0.004, 0.004, 0.003]
width_hist = 10.69  # ширина интервала
# набор данных для полигона
x_all_pol = [9.54, 20.23, 30.92, 41.61, 52.29, 62.98, 73.67, 84.36]
y_all_pol = [0.033, 0.023, 0.012, 0.010, 0.005, 0.004, 0.004, 0.003]

# создание фигуры
fig = plt.figure(figsize=(10, 9))
p = fig.add_subplot()
# гистограмма
p.bar(x_all_hist, y_all_hist, width=width_hist, align="edge", color="orange", linewidth=1.0, edgecolor="black", label='гистограмма')
# полигон
p.plot(x_all_pol, y_all_pol, color="red", marker="o", label='полигон')

# ПРВ экспоненциального распределения
la = 0.0353   # лямбда
step_exp = 0.0001
x_exp = np.arange(x_left_hist, x_right_hist, step_exp)
p.plot(x_exp, expon.pdf(x_exp, scale=28.328611898017), color="green", label='ПРВ экспоненциального распределения')
# scale = 1/лямбда

# легенда
plt.title("Графики для X: гистограмма, полигон, ПРВ для экспоненциального распределения")
plt.ylabel("n_i/(n*w)")
plt.xlabel("x")
plt.ylim(0, 0.0353)
p.legend(loc='upper right')
# отметки
x_all_unique = list(set([0] + x_all_hist + [x_right_hist] + x_all_pol))
y_all_unique = list(set(y_all_hist + y_all_pol + [la]))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
