class CountIntervals:

    def __init__(self):
        # keep the interval sorted and add will update the merge
        self.interval = [(-inf, -inf), (inf, inf)]
        self.cnt = 0
# time:O(nlogn+N)
    def add(self, left: int, right: int) -> None:
        idx = bisect.bisect_left(self.interval, left-1, key=lambda x:x[0])
        endIdx = bisect.bisect_left(self.interval, right+1, key=lambda x:x[0])
        n = len(self.interval)
        # the existing intv overlapped
        if self.interval[idx-1][1]>=left-1:
            idx -= 1
        lVal = min(self.interval[idx][0], left)
        rVal = max(self.interval[endIdx-1][1], right)

        toDel = 0
        for i in range(idx, endIdx):
            toDel += (self.interval[i][1]-self.interval[i][0]+1)
        self.cnt += (rVal-lVal+1 - toDel)
        self.interval[idx:endIdx] = [(lVal, rVal)]
# time:O(N)
    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()