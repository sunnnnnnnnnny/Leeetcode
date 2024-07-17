class Solution:
    # store the num to idx array, when encouter pick, randomly return one index
    def __init__(self, nums: List[int]):
        self.num2Idx = {}
        for i in range(len(nums)):
            if nums[i] not in self.num2Idx.keys():
                self.num2Idx[nums[i]] = []
            self.num2Idx[nums[i]].append(i)

    def pick(self, target: int) -> int:
        select = self.num2Idx[target]
        listIdx = random.randint(0,len(select)-1)
        return select[listIdx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)