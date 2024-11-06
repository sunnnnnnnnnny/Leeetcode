class Vector2D:
# time:O(1) space:O(N)
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = 0
        # need to find the first start idx
        while len(self.vec)>0 and len(self.vec[self.i])==0:
            self.j= 0
            self.i += 1
            if self.i == len(self.vec):
                break

    def next(self) -> int:
        ret = self.vec[self.i][self.j]
        self.j+=1
        while self.j == len(self.vec[self.i]):
            self.j= 0
            self.i += 1
            if self.i == len(self.vec):
                break
        return ret

    def hasNext(self) -> bool:
        if self.i == len(self.vec):
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()