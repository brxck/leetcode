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
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# @lc code=end
