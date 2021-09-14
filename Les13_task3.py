"""
В приложении к заданию дан модуль testing_example.py В модуле вы найдете класс Calculator, у которого есть
методы для выполнения простейших математических операций.
С помощью модулей unittest или pytest напишите тесты для методов этого класса.
Используйте фикстуры для того, чтобы создать объект класса Calculator, который вы будете использовать для
тестирования.
"""
import unittest
from testing_example import Calculator


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # Применение аналога фикстуры из pytest, создание объекта класса калькулятор
        cls.calculator = Calculator()

    def test_calc_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)

    def test_calc_mult(self):
        self.assertEqual(self.calculator.mult(2, 3), 6)

    def test_calc_sum_v2(self):
        self.assertEqual(self.calculator.sum(2, 5), 8)

    def test_calc_sum_v3(self):
        self.assertEqual(Calculator.sum(self, 2, 5), 8)


if __name__ == '__main__':
    unittest.main()
