"""Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

class Solution:
    # Solution using recursion
    def climbStairs_recursion(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_recursion(n-1) + self.climbStairs_recursion(n-2)

    # Solution using dynamic programing and recursion
    def climbStairs_dp(self, n: int) -> int:
        m={}

        def dynamic_p(n):
            if n < 3:
                return n
            if n not in m:
                m[n] = dynamic_p(n-1)+dynamic_p(n-2)
            return m[n]
        return dynamic_p(n)

    # Solution using table and dynamic programing
    def climbStairs_dp_table(self, n: int) -> int:
        if n==1:
            return 1
        result = [0]*n
        result[0] = 1
        result[1] = 2
        for i in range(2, n):
            result[i] = result[i-2]+result[i-1]
        return result[-1]


my_result = Solution()
print(my_result.climbStairs_recursion(6))
print(my_result.climbStairs_dp(6))
print(my_result.climbStairs_dp_table(6))