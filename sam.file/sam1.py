# Импортируем модуль datetime для работы с датой и временем.
from datetime import datetime
# Импортируем функцию sqrt из модуля math для вычисления квадратного корня.
from math import sqrt
# Определяем функцию main, которая принимает произвольное количество именованных аргументов.
def main(**kwargs):
    # Проходим по каждому ключ-значение в словаре kwargs.
    for key in kwargs.items():
        # Вычисляем длину вектора для текущего набора координат.
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Выводим результат.
        print(result)
# Проверяем, является ли текущий модуль точкой входа в программу.
if	__name__== '__main__':
    # Фиксируем время начала выполнения программы.
    start_time = datetime.now()
    # Вызываем функцию main с набором координат.
    main(one=[10, 3],
         two=[5, 4],
         three=[15, 13],
         four=[93, 53],
         five=[133, 15]
    )
# Вычисляем время, затраченное на выполнение программы.
time_costs = datetime.now() - start_time
# Выводим время выполнения программы.
print(f"Время выполнения программы - {time_costs}")