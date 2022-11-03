from algostructure.arrays.code.max_consec_ones import Solution
import unittest


class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def test_example_one(self):
        arr = [1, 1, 0, 1, 1, 1]
        result = Solution()
        self.assertEqual(result.findMaxConsecutiveOnes(arr), 3)

    def test_example_two(self):
        arr = [1, 0, 1, 1, 0, 1]
        result = Solution()
        self.assertEqual(result.findMaxConsecutiveOnes(arr), 2)
