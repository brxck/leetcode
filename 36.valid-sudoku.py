#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List

# @lc code=start
import math
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value == ".":
                    continue

                value = int(value)
                b = math.floor(c / 3) + math.floor(r / 3) * 3

                if value in rows[r] or value in columns[c] or value in boxes[b]:
                    return False

                rows[r].add(value)
                columns[c].add(value)
                boxes[b].add(value)

        return True


# @lc code=end

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

s = Solution()
print(s.isValidSudoku(board))
