#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for i in range(len(s)):
            j = i
            count = {}
            while j < len(s):
                count[s[j]] = count.get(s[j], 0) + 1
                window_length = j - i + 1
                valid = (window_length - max(count.values())) <= k
                if valid:
                    longest = max(window_length, longest)
                    j += 1
                else:
                    break
        return longest


# @lc code=end
s = Solution()
print(s.characterReplacement("ABAB", 2))
