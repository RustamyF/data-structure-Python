"""coin change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1
my_result=Solution()
coins = [1,2,5]; amount = 11
print(my_result.coinChange(coins, amount))


coins = [2]; amount = 3
print(my_result.coinChange(coins, amount))

coins = [1]; amount = 0
print(my_result.coinChange(coins, amount))
