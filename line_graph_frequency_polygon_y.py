# Полигон частот для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [6.38, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]
# создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график)
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# линейный график
p.plot(x_all, y_all, color="red", marker="o")
# легенда
plt.title("Полигон частот для Y")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
# отметки на осях с сеткой (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике)
x_all_unique, y_all_unique = list(set(x_all)), list(set(y_all))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()
# вывод
plt.show()
