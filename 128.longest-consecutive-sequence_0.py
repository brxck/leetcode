#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

from typing import List

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0

        for n in ns:
            length = 1
            if n - 1 not in ns:
                while n + length in ns:
                    length += 1
            if length > longest:
                longest = length

        return longest


# @lc code=end

s = Solution()
print(s.longestConsecutive([]))
print(s.longestConsecutive([1, 2, 0, 1]))
