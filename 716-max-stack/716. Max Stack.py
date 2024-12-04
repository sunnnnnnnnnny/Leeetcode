class MaxStack:
# getting the max elemtent with stack FILO
# need unique identify for each elementt by a separte dict to record the exsistence
# having maxHeap for the retriving the max
# list for regular stack operation
# counter for identifier
# space:O(3N) = O(N)
    def __init__(self):
        self.cnt = 0
        self.maxH = []
        self.stack = []
        self.exist = set()
# t:O(logN)
    def push(self, x: int) -> None:
        kid = self.cnt
        heapq.heappush(self.maxH, (-x, -kid))
        self.stack.append((x, kid))
        self.exist.add(kid)
        self.cnt += 1
# t:O(logN)
    def pop(self) -> int:
        while self.stack:
            val, kid = self.stack.pop()
            if kid in self.exist:
                self.exist.remove(kid)
                return val
        return 0
# t:O(1)   because the remove might never happens, amortized time would be O(1)
    def top(self) -> int:
        while self.stack:
            val, kid = self.stack[-1]
            if kid not in self.exist:
                self.stack.pop()
            else:
                return val
        return 0
# t:O(logN)
    def peekMax(self) -> int:
        while self.maxH:
            val, kid = self.maxH[0]
            if -kid not in self.exist:
                heapq.heappop(self.maxH)
            else:
                return -val
        return 0
# t:O(logN)
    def popMax(self) -> int:
        while self.maxH:
            val, kid = heapq.heappop(self.maxH)
            if -kid in self.exist:
                self.exist.remove(-kid)
                return -val
        return 0
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()