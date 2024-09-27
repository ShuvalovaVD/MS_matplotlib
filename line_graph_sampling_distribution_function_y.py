# Выборочная функция распределения для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [6.39, 10.57, 14.75, 18.93, 23.11, 27.29, 31.47, 35.65, 39.83, 44.01]
y_all = [0.10, 0.22, 0.37, 0.48, 0.57, 0.63, 0.75, 0.86, 0.92, 1.00]
# создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график)
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# стрелочки
p.scatter(x_all, y_all, marker="<", color="red")
# линии
for i in range(len(x_all) - 1):
    x_line = [x_all[i], x_all[i + 1]]
    y_line = [y_all[i], y_all[i]]
    p.plot(x_line, y_line, color="red")
# осталось достроить граничные линии для крайних точек x при y = 0 и y = 1: продлеваем их на l1 единиц влево и вправо
l1 = 3
p.plot([x_all[0] - l1, x_all[0]], [0, 0], color="red")
p.plot([x_all[-1], x_all[-1] + l1], [1, 1], color="red")
# устанавливаем границы графика на l2 (l2 < l1) единиц слева и справа от крайних точек x, чтобы обрезать линии
l2 = l1 - 1
plt.xlim(x_all[0] - l2, x_all[-1] + l2)
# легенда
plt.title("Выборочная функция распределения для Y")
plt.ylabel("F(y)")
plt.xlabel("y")
# отметки на осях с сеткой (нужны уникальные значения отметок, чтобы не было жирного наслоения на графике)
x_all_unique, y_all_unique = list(set(x_all)), list(set([0] + y_all))  # добавляем отметку y = 0, т. к. её нет в y_all
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()  # сетка
# вывод
plt.show()
