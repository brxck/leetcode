#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

from typing import List


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        a, b = 0, len(height) - 1
        left, right = height[a], height[b]
        total = 0
        while a < b:
            if left < right:
                total += left - height[a]
                a += 1
                left = max(left, height[a])
            else:
                total += right - height[b]
                b -= 1
                right = max(right, height[b])
        return total


# @lc code=ends

s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
