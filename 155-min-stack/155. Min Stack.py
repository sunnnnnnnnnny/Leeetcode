class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # having the min and cnt
        if len(self.minStack) == 0:
            self.minStack.append([val, 1])
        else:
            if self.minStack[-1][0]>val:
                self.minStack.append([val, 1])
            else:
                self.minStack[-1][1]+=1


    def pop(self) -> None:
        self.stack.pop()
        self.minStack[-1][1]-=1
        if self.minStack[-1][1] == 0:
            self.minStack.pop()

    def top(self) -> int:
       return self.stack[-1]
        

    def getMin(self) -> int:
        # need O(1) time thus need to keep track of the min so far
        return  self.minStack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()