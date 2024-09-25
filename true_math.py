# Пункты задачи:
# Создайте модули fake_math и true_math.


# Модуль true_math.py:

from math import inf

def divide(first, second):
    if second == 0:
        return inf
    return first / second