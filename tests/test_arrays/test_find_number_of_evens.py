from algostructure.arrays.code.find_number_of_evens import Solution
import unittest


class TestFindNumbers(unittest.TestCase):
    def test_example_one(self):
        arr = [12,345,2,6,7896]
        result = Solution()
        self.assertEqual(result.find_numbers(arr), 2)

    def test_example_two(self):
        arr = [555,901,482,1771]
        result = Solution()
        self.assertEqual(result.find_numbers(arr), 1)