#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List

# @lc code=start


class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        triplets = []

        for i in range(0, max(0, len(numbers))):
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                triplet = [numbers[i], numbers[j], numbers[k]]
                triplet_sum = sum(triplet)

                if triplet_sum == 0:
                    if triplet not in triplets:
                        triplets.append(triplet)
                    j += 1
                elif triplet_sum > 0:
                    k -= 1
                elif triplet_sum < 0:
                    j += 1

        return triplets


# @lc code=end

print(Solution.threeSum(None, [-1, 0, 1, 2, -1, -4]))
print(Solution.threeSum(None, [0, 0, 0, 0]))
print(Solution.threeSum(None, [-2, 0, 1, 1, 2]))
