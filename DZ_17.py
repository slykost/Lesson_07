# ДЗ 17. Функцию square

# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.


def square(s):
    return (s * 4, s ** 2, round(s * (2 ** 0.5), 2))

print(square(int(input('Введите число сторону квадрата: '))))