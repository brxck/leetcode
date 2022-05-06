#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# Didn't realize that sub strings could overlap ex
# "dvdvf" so we need two pointers


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        chars = set()
        for i in range(0, len(s)):
            j = i
            while j < len(s):
                if s[j] in chars:
                    chars.clear()
                    break
                chars.add(s[j])
                longest = max(len(chars), longest)
                j += 1
        return longest


# @lc code=end
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
