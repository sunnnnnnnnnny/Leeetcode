class Solution:
    # one idea of making the probability to ratio of weight, would be making a copy of w[i]*i element into an array
    # then call random based on the len of array
    # create a aggregate count array with same size as original, with the randon giving from 0~n
    # the array will be [x, y, z] its the upper bound of it, if x<p<=y then it's the secound index
    # time:O(N+logN) space:O(N)
    def __init__(self, w: List[int]):
        self.counter = [0 for i in range(len(w))]
        self.counter[0] = w[0]
        for i in range(1, len(w)):
            self.counter[i] = self.counter[i-1]+w[i]

    def pickIndex(self) -> int:
        # now = random.uniform(1,self.counter[-1])
        now = self.counter[-1] * random.random()
        # run a binary search to find the target zone
        # low, high = 0, len(self.counter)
        # while low < high:
        #     mid = low + (high - low) // 2
        #     if now > self.counter[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid
        # return low
        idx = bisect.bisect_left(self.counter, now)
        ret = idx
        if self.counter[idx] < now:
            ret = idx+1
        
        # print(now, idx, self.counter[idx], ret)
        return ret
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()