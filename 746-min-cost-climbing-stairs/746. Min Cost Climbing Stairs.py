class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min(dp[i-1], dp[i-2])
        dp = [-1]*(len(cost)+1)
        dp[0] = dp[1] = 0
        for i in range(2, len(cost)+1, 1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

        