#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
class MinStack:
    def __init__(self):
        self.items = []
        self.minimum = []

    def push(self, val: int) -> None:
        min_val = min(self.minimum[-1], val) if self.minimum else val
        self.minimum.append(min_val)
        self.items.append(val)

    def pop(self) -> None:
        self.minimum.pop()
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
