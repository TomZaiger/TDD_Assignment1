import unittest
from BMI_Calculator import *


class Test_BMI_Category_Calculator(unittest.TestCase):
    def test_bmi_value_calculator(self):
        bmi = -20.5

        self.assertRaises(ValueError, calculate_bmi_category, bmi)


class Test_BMI_Value_Calculator(unittest.TestCase):
    def test_enter_character(self):
        weight = 'a'
        height = 1.81

        self.assertRaises(ValueError, calculate_bmi, weight, height)


if __name__ == '__main__':
    unittest.main()
