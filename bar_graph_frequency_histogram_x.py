# Гистограмма частот для СВ X
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [1.99, 3.96, 5.93, 7.90, 9.87, 11.84, 13.81, 15.78, 17.75, 19.72]  # те x, к-рые слева от столбиков
y_all = [0.04, 0.06, 0.10, 0.10, 0.05, 0.04, 0.03, 0.04, 0.03, 0.03]
# создание фигуры
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# столбчатая диаграмма
p.bar(x_all, y_all, width=1.97, align="edge", color="orange", linewidth=1.0, edgecolor="black")  # указываем ширину
# легенда
plt.title("Гистограмма частот для СВ X")
plt.ylabel("n_i/(n*w)")
plt.xlabel("x")
# отметки
p.xaxis.set_major_locator(FixedLocator(x_all + [21.69]))  # добавила самое правое значение
p.yaxis.set_major_locator(FixedLocator(y_all))
# вывод
plt.show()