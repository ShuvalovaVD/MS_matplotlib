# График безубыточности для РГР по бизнес-планированию
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
# наборы данных
x_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_all_1 = [2000] * 12
y_all_2 = [30.336, 45.504, 60.672] + [75.840] * 9
y_all_3 = [2030.336, 2045.504, 2060.672] + [2075.840] * 9
y_all_4 = [24000, 36000, 48000] + [60000] * 9
# создание фигуры
fig = plt.figure(figsize=(10, 6))
p = fig.add_subplot()
# построение линейных графиков
p.plot(x_all, y_all_1, color="blue", marker="D", label="постоянные затраты")
p.plot(x_all, y_all_2, color="purple", marker="s", label="переменные затраты")
p.plot(x_all, y_all_3, color="yellow", marker="^", label="совокупные затраты")
p.plot(x_all, y_all_4, color="cyan", marker="o", label="выручка")
# легенда
plt.title("График безубыточности")
plt.ylabel("руб.")
plt.xlabel("мес.")
p.legend(loc='center right')
# сетка
x_all_unique, y_all_unique = list(set(x_all)), list(set([60, 2000] + y_all_4))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
p.grid()
# вывод
plt.show()
