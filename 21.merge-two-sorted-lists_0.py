#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @lc code=start


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        while list1 or list2:
            # We can optimize/simplify this
            # End loop if one of the lists does not exist
            # Link remaining list to result tail
            if not list2 or (list1 and list1.val <= list2.val):
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        return res.next


# @lc code=end
