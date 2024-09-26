# Гистограмма частот для X
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [1.99, 3.96, 5.93, 7.90, 9.87, 11.84, 13.81, 15.78, 17.75, 19.72]  # те координаты x, к-рые слева от столбиков
x_right = 21.69  # тот x, к-рый идёт после всех столбиков
y_all = [0.04, 0.06, 0.10, 0.10, 0.05, 0.04, 0.03, 0.04, 0.03, 0.03]  # значения столбиков по y, соответствуют x_all
# создание фигуры, на которой будут размещаться графики (в нашем случае - один график)
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# столбчатая диаграмма
width = x_all[1] - x_all[0]  # ширина столбиков по x
p.bar(x_all, y_all, width=width, align="edge", color="orange", linewidth=1.0, edgecolor="black")
# легенда
plt.title("Гистограмма частот для X")
plt.ylabel("n_i/(n*w)")
plt.xlabel("x")
# отметки на осях (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике => множество set)
x_all_unique, y_all_unique = list(set(x_all + [x_right])), list(set(y_all))  # добавила самое правое значение x_right
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
