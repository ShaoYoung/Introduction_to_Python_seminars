# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Задать список из n чисел последовательности  (1 + 1/n)^n и вывести на экран их сумму

# Задание списка из n чисел последовательности
def get_list(n):
    list = []
    # mystr = list() - альтернативный вариант задания списка
    for i in range(1, n + 1):
        list.append(round((1 + 1 / i) ** i, 2))
    return list


# Вычисление суммы элементов списка
def sum_list(list):
    result = 0
    for i in list:
        result += i
    return result


n = int(input("Введите число n "))
list = get_list(n)
print(f"Список {list}")
print(f"Сумма элементов списка {sum_list(list)}")