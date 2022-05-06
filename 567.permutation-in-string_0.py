#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1

        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1) - 1

            # Constructing map every iteration = O(n^2)?
            # We construct the window map once and then just update it
            window = {}
            for i in range(l, r + 1):
                window[s2[i]] = window.get(s2[i], 0) + 1

            if window == target:
                return True

        return False


# @lc code=end

print(Solution().checkInclusion("adc", "dcda"))
