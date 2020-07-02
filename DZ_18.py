# ДЗ 18. Функцию season

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).


def season(month):
        if month in (3, 4, 5):
            return 'Весна'
        elif month in (6, 7, 8):
            return 'Лето'
        elif month in (9, 10, 11):
            return 'Осень'
        elif month in (12, 1, 2):
            return 'Зима'
        else:
            return 'Неверный Ввод! Введите число от 1 до 12'


month = int(input('Введите номер месяца: '))
print(season(month))
