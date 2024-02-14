import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
# все опорные точки для сетки
x_all = [7.5, 12.5, 17.5, 22.5]
y_all = [0.2, 0.4, 0.9]
# точки для стрелочек
x_points = [7.5, 12.5, 17.5]
y_points = [0.2, 0.4, 0.9]
# создание фигуры
fig = plt.figure()
p = fig.add_subplot()
# стрелочки
p.scatter(x_points, y_points, marker="<")
# линии
for i in range(len(x_all) - 1):
    x_line = [x_all[i], x_all[i + 1]]
    y_line = [y_all[i], y_all[i]]
    p.plot(x_line, y_line, color="blue")
# бесконечные линии влево и вправо
p.plot([6, 7.5], [0, 0], color="blue")
p.plot([22.5, 23], [0.9, 0.9], color="blue")
# легенда
plt.ylabel("F(x)")
plt.xlabel("x")
# сетка
p.xaxis.set_major_locator(FixedLocator(x_all))
p.yaxis.set_major_locator(FixedLocator([0] + y_all))
p.grid()
# вывод
plt.show()
