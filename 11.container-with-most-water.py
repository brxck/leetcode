#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        largest = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > largest:
                largest = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return largest


# @lc code=end
s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
