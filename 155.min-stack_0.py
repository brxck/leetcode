#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# This solution is more complicated but uses less space and time

# @lc code=start
class MinStack:
    def __init__(self):
        self.items = []
        self.minimum = None
        self.count = 0

    def push(self, val: int) -> None:
        if self.count < 1 or val < self.minimum:
            self.minimum = val
            self.count = 1
        elif val == self.minimum:
            self.count += 1

        self.items.append(val)

    def pop(self) -> None:
        val = self.items.pop()
        if val == self.minimum:
            if not self.items:
                self.count = 0
            elif self.count == 1:
                self.minimum = min(self.items)
                self.count = self.items.count(self.minimum)
            else:
                self.count -= 1

        return val

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minimum if self.count > 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
