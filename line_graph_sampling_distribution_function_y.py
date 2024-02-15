# Выборочная функция распределения для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [6.39, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all = [0.10, 0.22, 0.38, 0.54, 0.63, 0.70, 0.78, 0.85, 0.92, 1.00]
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
p.xaxis.set_major_locator(FixedLocator(x_all))
p.yaxis.set_major_locator(FixedLocator([0] + y_all))
p.grid()
# вывод
plt.show()
