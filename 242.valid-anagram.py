#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first = {}
        second = {}

        letters = zip(s, t)

        for a, b in letters:
            first[a] = first.get(a, 0) + 1
            second[b] = second.get(b, 0) + 1

        return first == second


# @lc code=end
