from algostructure.arrays.code.rotated_sorted_array import Solution
import unittest


class TestRotatedSortedArray(unittest.TestCase):
    def test_example_one(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        result = Solution()
        self.assertEqual(result.search(nums, target), 4)

    def test_example_two(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        result = Solution()
        self.assertEqual(result.search(nums, target), -1)


