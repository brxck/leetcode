#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List

# @lc code=start
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(lambda: 0)
        top = [[] for _ in range(0, len(nums) + 1)]

        for n in nums:
            frequency[n] += 1
        for v, f in frequency.items():
            top[f].append(v)

        result = []
        for i in range(len(top) - 1, 0, -1):
            for v in top[i]:
                result.append(v)
                if len(result) == k:
                    return result


# @lc code=end

s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
