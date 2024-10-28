class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()

        if popped == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return none

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return none
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()