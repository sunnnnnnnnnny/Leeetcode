class Solution:

    def __init__(self, nums: List[int]):
        # record the original string
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ret = list(self.nums)
        for i in range(len(ret)):
            randomIdx = random.randrange(i,len(ret))
            ret[i], ret[randomIdx] = ret[randomIdx], ret[i]
        return ret
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()