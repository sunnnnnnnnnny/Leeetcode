class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2]+n, dp[i-1])
        # time:O(n) spcaeLO(n) bottomup
        if len(nums) == 0:
            return 0
        dp = [[0,0] for i in range(len(nums))]
        dp[0] = nums[0]
        houseN = len(nums)
        if houseN>=2:
            dp[1] = max(nums[1],nums[0])
        for house in range(2, len(nums)):
            # max of previous available node
            dp[house] = max(dp[house-1],dp[house-2]+nums[house])
        print(dp)
        return dp[-1]
