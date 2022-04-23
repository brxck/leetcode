#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
import json
from typing import List

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for str in strs:
            count = {}
            for letter in str:
                count[letter] = count.get(letter, 0) + 1
            count_hash = json.dumps(count, sort_keys=True)
            counts[count_hash] = counts.get(count_hash, []) + [str]

        return list(counts.values())


# @lc code=end


x = Solution()
print(x.groupAnagrams(["ddddddddddg", "dgggggggggg"]))
