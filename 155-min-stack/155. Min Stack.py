class MinStack:
    # only retrieve min need constant time, using a val to record the min
    # only after pop we need to get the min again ->O(n)
    # push O(1) because only compare the min to pushed element
    # top is ordered, thus is easy

    def __init__(self):
        self.arr = []
        self.curMin = 0

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.curMin = val
        else:
            self.curMin = min(self.curMin, val)
        self.arr.append(val)
        
    def pop(self) -> None:
        if len(self.arr) > 0:
            removeVal = self.arr.pop(-1)
            if self.curMin == removeVal and len(self.arr)>0:
                self.curMin = min(self.arr)
        

    def top(self) -> int:
        if len(self.arr) > 0:
            return self.arr[-1]
       
        

    def getMin(self) -> int:
        return self.curMin

