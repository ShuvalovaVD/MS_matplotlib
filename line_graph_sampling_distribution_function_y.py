# Выборочная функция распределения для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [6.39, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all = [0.10, 0.22, 0.37, 0.48, 0.57, 0.63, 0.75, 0.86, 0.92, 1.00]
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
plt.title("Выборочная функция распределения для Y")
plt.ylabel("F(y)")
plt.xlabel("y")
# сетка
x_all_unique, y_all_unique = list(set(x_all)), list(set([0] + y_all))  # добавила 0 для оси Ox
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()
# вывод
plt.show()
