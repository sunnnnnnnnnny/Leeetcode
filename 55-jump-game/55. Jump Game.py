class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy, check if the any of the left most position can be reached
        # no need to care if there's multiple way to get there
        # lastIdx = len(nums)-1
        # for i in range(len(nums)-2, -1,-1):
        #     # as long as it can jump over lastIdx, then we are good
        #     if i+nums[i]>=lastIdx:
        #         lastIdx = i
        # return lastIdx == 0
        # #  dp[i] meaning if we can jump to that location
        # # dp[i] = true if j+jump[j]>i and dp[j]==true while i>j
        # # or bottom up to populate the dp
        # # time:O(N^N) space:O(N)
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(len(nums)):
            # d[i]>0 meaning we can be at this location
            if dp[i]>0:
                for j in range(1,nums[i]+1):
                    if i+j<len(nums):
                        dp[i+j] = 1
                    if i+j==len(nums)-1:
                        return True
        return True if dp[-1]>0 else False
