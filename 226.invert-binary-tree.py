#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root


# @lc code=end
