class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] = sum(dp[i-coin]) -> not 1D dp
        # how to remove duplicates 
        # dp[i][j] = stores the number of ways to make up the j amount using the coins beginning from index i
        # dp[i][j] = dp[i+1][j] if coin[i]>j thus not selecting coin i
        # dp[i][j] = dp[i][j-coin[i]]+dp[i+1][j] of both select and not select
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        # setting the base as amount 0 for all coin type is 1 way (not select)
        for idxC in range(len(coins)):
            dp[idxC][0] = 1
        # this way of building the amount with only the coins of other index
        # allowing the unique way of making it
        for idxC in range(len(coins)-1, -1, -1):
            for buildAmt in range(1, amount+1, 1):
                if coins[idxC]>buildAmt:
                    dp[idxC][buildAmt] = dp[idxC+1][buildAmt]
                else:
                    dp[idxC][buildAmt] = dp[idxC+1][buildAmt]+dp[idxC][buildAmt-coins[idxC]]
        # print(dp)
        return dp[0][amount]
                

        