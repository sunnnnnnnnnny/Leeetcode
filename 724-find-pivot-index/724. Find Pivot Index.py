class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # pre calculate the sume from the right and record
        # then check it from the left to get the left most idx
        # time:O(N) space:O(N)
        n = len(nums)
        rightSum = [0]*n
        for i in range(n-2,-1, -1):
            rightSum[i] = rightSum[i+1]+nums[i+1]
        # print(rightSum)
        nowSum = 0
        for i in range(n):
            if nowSum == rightSum[i]:
                return i
            nowSum += nums[i]
        return -1