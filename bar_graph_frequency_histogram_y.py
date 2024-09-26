# Гистограмма частот для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [4.30, 8.48, 12.66, 16.84, 21.02, 25.20, 29.38, 33.56, 37.74, 41.92]  # координаты x, к-рые слева от столбиков
x_right = 46.10  # тот x, к-рый идёт после всех столбиков
y_all = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]  # значения столбиков по y, соответствуют x_all
# создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график)
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# столбчатая диаграмма
width = x_all[1] - x_all[0]  # ширина столбиков по x
p.bar(x_all, y_all, width=width, align="edge", color="orange", linewidth=1.0, edgecolor="black")
# легенда
plt.title("Гистограмма частот для Y")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
# отметки на осях (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике => множество set)
x_all_unique, y_all_unique = list(set(x_all + [x_right])), list(set(y_all))  # добавила самое правое значение x_right
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
