class Solution:
    def climbStairs(self, n: int) -> int:
        # dp bottom up to calculate the steps
        # dp[i] = dp[i-1]+dp[i-2]
        # time:O(N) space:O(N)
        # save space only use 2 var to record the i-1, i-2
        # time:O(N) space:O(1)
        # dp = [0 for _ in range(n+1)]
        if n<1:
            return 0
        # dp[0] = dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1]+dp[i-2]
        dp0 = dp1 = 1
        now = 0
        for i in range(2, n+1):
            now = dp0+dp1
            dp0 = dp1
            dp1 = now
        return dp1
