#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_by_diff = {}
        for i, v in enumerate(numbers):
            if v in index_by_diff:
                return [index_by_diff[v], i]
            else:
                index_by_diff[target - v] = i


# @lc code=end

print(Solution.twoSum(None, [2, 7, 11, 15], 9))
