class NumArray:
# get the prefixSum of the array
# time:O(N) space:O(N)
# get takes only O(1)
    def __init__(self, nums: List[int]):
        self.prefixSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefixSum[i+1] = self.prefixSum[i]+nums[i]
        self.n = len(nums)
    def sumRange(self, left: int, right: int) -> int:
        if right>=self.n:
            return -1
        return self.prefixSum[right+1]-self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)