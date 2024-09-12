class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min of all coins (dp[c]+1)
        # time:O(amount*coins)
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for c in coins:
            if c < amount+1:
                dp[c] = 1
        for i in range(1, amount+1):
            if dp[i] == -1:
                continue
            for c in coins:
                nextC = i+c
                if nextC<amount+1:
                    dp[nextC] = dp[i]+1 if dp[nextC]<0 else min(dp[nextC],dp[i]+1)
        
        return dp[amount]