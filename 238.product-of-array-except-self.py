#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1 for _ in nums], [1 for _ in nums]
        for i in range(0, len(nums)):
            j = len(nums) - i - 1
            if i + 1 < len(nums):
                left[i + 1] = nums[i] * left[i]
            if j - 1 >= 0:
                right[j - 1] = nums[j] * right[j]

        res = []
        for l, r in zip(left, right):
            res.append(l * r)
        return res


# @lc code=end


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
