class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal:
            minV = min(self.minVal[-1], val)
            self.minVal.append(minV)
        else:
            self.minVal.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()