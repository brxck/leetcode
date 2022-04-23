#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, 1
        profit = 0

        while b < len(prices):
            if prices[a] < prices[b]:
                profit = max(profit, prices[b] - prices[a])
            elif prices[a] > prices[b]:
                a = b
            b += 1

        return profit


# @lc code=end
