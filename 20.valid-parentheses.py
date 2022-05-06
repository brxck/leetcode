#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in pairs:
                stack.append(c)
                continue

            try:
                if pairs[stack.pop()] != c:
                    return False
            except IndexError:
                return False

        return len(stack) == 0


# @lc code=end
