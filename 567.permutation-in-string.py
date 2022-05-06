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

        window = {}
        for i in range(0, len(s1) - 1):
            window[s2[i]] = window.get(s2[i], 0) + 1

        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1) - 1
            window[s2[r]] = window.get(s2[r], 0) + 1

            if window == target:
                return True
            elif window[s2[l]] == 1:
                window.pop(s2[l])
            else:
                window[s2[l]] -= 1

        return False


# @lc code=end

print(Solution().checkInclusion("adc", "dcda"))
