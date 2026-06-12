class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, value: int) -> None:
        if (len(self.minStack) == 0):
            self.minStack.append([value, value])
        
        else:
            minVal = min(self.minStack[-1][1], value)
            self.minStack.append([value, minVal])
        

    def pop(self) -> None:
        self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1][0]
        

    def getMin(self) -> int:
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()