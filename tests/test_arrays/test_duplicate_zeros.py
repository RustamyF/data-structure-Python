from algostructure.arrays.code.duplicate_zeros import Solution
import unittest


class TestDuplicateZeros(unittest.TestCase):
    def test_example_one(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        result = Solution()
        self.assertEqual(result.duplicate_zeros(arr), [1, 0, 0, 2, 3, 0, 0, 4])

    def test_example_two(self):
        arr = [1, 2, 3]
        result = Solution()
        self.assertEqual(result.duplicate_zeros(arr), [1, 2, 3])
