class Solution:
    def tribonacci(self, n: int) -> int:
        # DP 
        if n == 0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1, 1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            # print('i:, dp:', i, dp[i])
        return dp[n]

        