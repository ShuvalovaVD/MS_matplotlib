# Выборочная функция распределения для X
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [2.98, 4.95, 6.92, 8.89, 10.86, 12.83, 14.80, 16.77, 18.74, 20.71]
y_all = [0.07, 0.19, 0.39, 0.58, 0.67, 0.74, 0.80, 0.88, 0.94, 1.00]
# создание фигуры
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# стрелочки
p.scatter(x_all, y_all, marker="<", color="red")
# линии
for i in range(len(x_all) - 1):
    x_line = [x_all[i], x_all[i + 1]]
    y_line = [y_all[i], y_all[i]]
    p.plot(x_line, y_line, color="red")
# бесконечные линии влево и вправо (всё равно придется фотошопить)
p.plot([x_all[0] - 2, x_all[0]], [0, 0], color="red")
p.plot([x_all[-1], x_all[-1] + 2], [y_all[-1], y_all[-1]], color="red")
# легенда
plt.title("Выборочная функция распределения для X")
plt.ylabel("F(x)")
plt.xlabel("x")
# сетка
x_all_unique, y_all_unique = list(set(x_all)), list(set([0] + y_all))  # добавила 0 для оси Ox
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()
# вывод
plt.show()
