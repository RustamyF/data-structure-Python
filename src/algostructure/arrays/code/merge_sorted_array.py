""""              Merge Sorted Array
Problem statement
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array 
nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Test case 1
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Test case 2
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

##### Solution
The problem can be solved an easy way using sorted function in python. We take the slice of nums1 from 0 to m and 
combine it with nums2 and return the sorted result. I can be done in one line of code. Here we are using a built in
function of python. What if we are not allowed to use built-in functions? The second method is created to solve the 
problem using two pointer algorithm. It is a little hard, but if we track our pointers, we can solve it.
"""""


class Solution:
    def merge_easy(self, nums1, m, nums2, n) -> None:
        return sorted(nums1[:m] + nums2)

    def merge(self, nums1, m, nums2, n):
        # copy the non zero elements from nums1
        copy = nums1[:m]
        # create two pointers one for nums1 and one for nums2
        l1 = 0
        l2 = 0
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that l1 and l2 aren't over the boundaries
            # of their respective arrays.
            if l2 >= n or (l1 < m and copy[l1] <= nums2[l2]):
                nums1[p] = copy[l1]
                l1 += 1
            else:
                nums1[p] = nums2[l2]
                l2 += 1
        return nums1
