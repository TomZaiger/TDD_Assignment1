import unittest
from Bubble_Sort import *


class Test_Bubble_Sort(unittest.TestCase):
    def test_returning_value(self):
        arr = [15, 30, 22, 72, 1, 3, 2, 14, 92, 46]

        sorted_arr = bubble_sort(arr)

        self.assertNotEqual(None, bubble_sort(arr))


    def test_returning_same_array_size(self):
        arr = [15, 30, 22, 72, 1, 3, 2, 14, 92, 46]

        sorted_arr = bubble_sort(arr)

        self.assertEqual(arr.__len__(), sorted_arr.__len__())


    def test_returning_same_values(self):
        arr = [15, 30, 22, 72, 1, 3, 2, 14, 92, 46]

        sorted_arr = bubble_sort(arr)

        self.assertCountEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
