# Полигон частот для X
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [2.98, 4.95, 6.92, 8.89, 10.86, 12.83, 14.80, 16.77, 18.74, 20.71]
y_all = [0.04, 0.06, 0.10, 0.10, 0.05, 0.04, 0.03, 0.04, 0.03, 0.03]
# создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график)
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# линейный график
p.plot(x_all, y_all, color="red", marker="o")
# легенда
plt.title("Полигон частот для X")
plt.ylabel("n_i/(n*w)")
plt.xlabel("x")
# отметки на осях с сеткой (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике)
x_all_unique, y_all_unique = list(set(x_all)), list(set(y_all))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()  # сетка
# вывод
plt.show()
