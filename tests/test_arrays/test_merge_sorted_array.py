from algostructure.arrays.code.merge_sorted_array import Solution
import unittest


class TestMergeSortedArray(unittest.TestCase):
    def test_example_one(self):
        nums1, m = [1, 2, 3, 0, 0, 0], 3
        nums2, n = [2, 5, 6], 3
        result = Solution()
        self.assertEqual(result.merge(nums1, m, nums2, n), [1, 2, 2, 3, 5, 6])

    def test_example_two(self):
        nums1, m = [1], 1
        nums2, n = [], 0
        result = Solution()
        self.assertEqual(result.merge(nums1, m, nums2, n), [1])
