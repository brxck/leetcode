#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalpha()]
        for i in range(0, len(chars)):
            j = len(chars) - i - 1
            if chars[i] != chars[j]:
                return False
            if i >= j:
                return True
        return True


# @lc code=end
