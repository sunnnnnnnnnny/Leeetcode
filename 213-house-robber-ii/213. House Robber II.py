class Solution:
    def rob(self, nums: List[int]) -> int:
        # treat as the same with breaking down the house
        # since house[1] house[n] are next to each other
        # the max would be (1-n-1) or (2-n)
        # dp[i] = max(dp[i-1], dp[i-2]+n[i])
        # time:O(2N) = O(N) space:O(1) if we keep only the pre and pre-1
        N = len(nums)
        if N == 0:
            return 0
        elif N== 1:
            return nums[0]
        elif N==2:
            return max(nums[0], nums[1])
        
        prev0 = nums[0]
        prev1 = max(nums[0], nums[1])
        maxSumN1 = max(prev0, prev1)
        for i in range(2,N-1):
            maxSumN1 = max(prev0+nums[i], prev1)
            prev0 = prev1
            prev1 = maxSumN1
        
        maxSumN2 = 0
        prev0 = 0
        prev1 = nums[1]
        maxSumN2 = max(prev0, prev1)
        for i in range(2,N):
            maxSumN2 = max(prev0+nums[i], prev1)
            prev0 = prev1
            prev1 = maxSumN2
        return max(maxSumN2, maxSumN1)