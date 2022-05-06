#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        while head:
            if head in seen:
                return True
            seen.append(head)
            head = head.next
        return False


# @lc code=end
