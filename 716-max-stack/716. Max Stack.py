class MaxStack:
# using 2 struct to store, the queue as regular, max stack for the max
# keep record if it's earse from the max stack
# time:O() space:O(2N)
    def __init__(self):
        self.cnt = 0
        self.maxS = []
        self.Q = []
        self.sErase = {}

    def push(self, x: int) -> None:
        # time:O(1)
        self.Q.append((x,self.cnt))
        heapq.heappush(self.maxS, (-x,-self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        # time:O(N)
        now = self.Q.pop()
        ret = now[0]
        findI = now[1]
        while findI>=0:
            ret = now[0]
            findI = now[1]
            if findI in self.sErase.keys():
                del self.sErase[findI]
                now = self.Q.pop()
            else:
                self.sErase[findI] = now
                break
        return ret
        
    def top(self) -> int:
        # time:O(N)
        now = self.Q[-1]
        ret = now[0]
        findI = now[1]
        while findI>=0:
            now = self.Q[-1]
            ret = now[0]
            findI = now[1]
            if findI in self.sErase.keys():
                del self.sErase[findI]
                self.Q.pop()
            else:
                break
        return ret

    def peekMax(self) -> int:
        # time:O(NlogN)
        now = self.maxS[0]
        ret = now[0]
        while self.maxS:
            now = self.maxS[0]
            idx = -now[1]
            ret = now[0]
            if idx in self.sErase.keys():
                heapq.heappop(self.maxS)
            else:
                break
                
        return -ret
    
    def popMax(self) -> int:
        # time:O(NlogN)
        # print(self.maxS)
        # print(self.sErase)
        now = self.maxS[0]
        ret = now[0]
        while self.maxS:
            now = self.maxS[0]
            idx = -now[1]
            ret = now[0]
            if idx in self.sErase.keys():
                heapq.heappop(self.maxS)
            else:
                self.sErase[idx] = -ret
                heapq.heappop(self.maxS)
                break

        return -ret
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()