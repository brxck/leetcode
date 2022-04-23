#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List

# @lc code=start


class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        seen = set()
        for n in numbers:
            if n in seen:
                return True
            seen.add(n)
        return False


# @lc code=end
