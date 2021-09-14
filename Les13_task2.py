def calculate_credit(s, r, n):
    try:
        if s >= 0 and r >= 0 and n >= 0:  # Проверка, что переданные числа больше 0
            r = r / 12
            result = int(s * (r * (1 + r) ** n) / ((1 + r) ** n - 1))
            return result
        else:
            return 'Исходные данные должны быть числами больше 0'
    except ZeroDivisionError:  # Обработка ошибки деления на ноль
        return 'На ноль делить нельзя!!!'
    except TypeError:  # Обработка ошибки, если исходные данные не являются числами
        return 'В исходных данных что-то отличное от числа!!!'


if __name__ == '__main__':  # Указание запустить код, если он выполняется как автономный файл.
    print(calculate_credit(0, 0, 0))
    print(calculate_credit(10, 0, 0))
    print(calculate_credit(10, 'abc', -100))
    print(calculate_credit(10, 0.5, 0))
    print(calculate_credit(10, 0.5, 6))
    print(calculate_credit(10, 0.5, -6))
    print(calculate_credit(-10, -0.5, -6))
    print(calculate_credit(-10, -0.5, 6))
    print(calculate_credit(20, 0.5, 6))
    print(calculate_credit('20', 0.5, 6))
    print(calculate_credit(20, 0.5, [6, 7, 8]))


