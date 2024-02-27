# Гистограмма частот для Y
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# набор данных
x_all = [4.30, 8.48, 12.66, 16.84, 21.02, 25.20, 29.38, 33.56, 37.74, 41.92]  # те x, к-рые слева от столбиков
y_all = [0.02, 0.03, 0.04, 0.03, 0.02, 0.01, 0.03, 0.03, 0.01, 0.02]
# создание фигуры
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# столбчатая диаграмма
p.bar(x_all, y_all, width=4.18, align="edge", color="orange", linewidth=1.0, edgecolor="black")  # указываем ширину
# легенда
plt.title("Гистограмма частот для Y")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
# отметки
x_all_unique, y_all_unique = list(set(x_all + [46.10])), list(set(y_all))  # добавила самое правое значение
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
