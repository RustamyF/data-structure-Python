from algostructure.arrays.code.valid_mountain import Solution
import unittest


class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def test_example_one(self):
        arr = [0, 3, 2, 1]
        result = Solution()
        self.assertEqual(result.validMountainArray(arr), True)

    def test_example_two(self):
        arr = [3, 5, 5]
        result = Solution()
        self.assertEqual(result.validMountainArray(arr), False)
