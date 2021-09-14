"""
В приложении к заданию дан модуль testing_example.py В модуле вы найдете функцию calculate_credit для расчета
месячного платежа по кредиту.
Напишите для этой функции набор тестов используя модуль unittest.
Ваши тесты должны учитывать как нормальный вариант работы функции, так и как можно большее число ошибочных
вызовов этой функции.
"""
import unittest
import random
from testing_example import calculate_credit

class Test_testing_example(unittest.TestCase):
    def test_type_1(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(random.randint(1, 1000000), random.uniform(0.0, 1.0), random.randint(1, 60))
        self.assertEqual(type(credit), int)  # Проверяем тип результата выполнения функции

    def test_type_2(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(random.randint(1, 1000000), random.uniform(0.0, 1.0), random.randint(1, 60))
        self.assertEqual(type(credit), float)  # Проверяем тип результата выполнения функции

    def test_equal_1(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(random.randint(1, 1000000), random.uniform(0.0, 1.0), random.randint(1, 60))
        self.assertEqual(credit, 10000)  # Проверяем равенство результата выполнения функции и числа

    def test_equal_2(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(random.randint(1, 1000000), random.uniform(0.0, 1.0), random.randint(1, 60))
        self.assertNotEqual(credit, 10000)  # Проверяем неравенство результата выполнения функции и числа

    def test_3(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(random.randint(-1000000, 0), random.uniform(0.0, 1.0), random.randint(1, 60))
        self.assertGreaterEqual(credit, 0)  # Проверяем что результат выполнения функции больше либо равен нулю

    def test_4(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(15000, -0.5, -10)
        self.assertGreaterEqual(credit, 0)  # Проверяем что результат выполнения функции больше либо равен нулю

    def test_none_1(self):  # Тестовые методы начинаются с префикса test_, сообщаем Python, что это методы тестирования
        credit = calculate_credit(10000, -0.5, -10)
        self.assertIsNone(credit)  # Проверяем что результат выполнения функции является None


if __name__ == '__main__':  # Указание запустить код, если он выполняется как автономный файл.
    unittest.main()

