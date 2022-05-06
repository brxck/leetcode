#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            length = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if (length - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
                length -= 1
            longest = max(longest, length)
        return longest


# @lc code=end
