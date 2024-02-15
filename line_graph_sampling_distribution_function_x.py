# Выборочная функция распределения для X
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [2.975, 4.945, 6.915, 8.885, 10.855, 12.825, 14.795, 16.765, 18.735, 20.705]
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
p.xaxis.set_major_locator(FixedLocator(x_all))
p.yaxis.set_major_locator(FixedLocator([0] + y_all))
p.grid()
# вывод
plt.show()
