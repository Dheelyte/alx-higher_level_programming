import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([1, -10, -5, 2, -5]), 2)

    def test_float_list(self):
        self.assertEqual(max_integer([1.0, 1.1, 1.2, 1.3, 1.4]), 1.4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
