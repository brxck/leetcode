#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# Find lowest price, followed by maximum price. Order is important.
# Two pointers. Left tracks lowest, right searches for highest.
# If left > right, move left to the new lowest price right
# Otherwise, continue searching for higher price with right

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(prices[r] - prices[l], profit)
            r += 1
        return profit


# @lc code=end
