#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# @lc code=start

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right)
        
        return
              
        
# @lc code=end

