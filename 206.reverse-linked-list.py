#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tail = curr.next
            curr.next = prev
            prev = curr
            curr = tail
        return prev


# @lc code=end
