#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            mid = ((upper - lower) // 2) + lower
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                return mid
        return -1


# @lc code=end
