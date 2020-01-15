import unittest
from Bubble_Sort import *


class Test_Bubble_Sort(unittest.TestCase):
    def test_returning_same_array_size(self):
        arr = [15, 30, 22, 72, 1, 3, 2, 14, 92, 46]
        size = arr.__len__

        new_arr = bubble_sort(arr)
        new_size = new_arr.__len__

        self.assertEqual(size, new_size)


if __name__ == '__main__':
    unittest.main()
