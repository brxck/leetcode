#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List

# Two pointers. Track max seen & add water trapped.
# Trach the largest left and right heights
# water_trapped[i] = min(max_left, max_right) - height[i]

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        water = 0
        while l < r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            if height[l] <= height[r]:
                water += min(max_left, max_right) - height[l]
                l += 1
            else:
                water += min(max_left, max_right) - height[r]
                r -= 1
        return water


# @lc code=end
