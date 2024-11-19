class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # count the linked characters, with n*m 
        # dp[i][j] = max(dp[i+1][j], dp[i][j+1]) 
        # if char i==j, dp[i+1][j+1]+1
        # time:O(N*M) space:O(N*M)
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m+1)]for _ in range(n+1)]
        # if the other word is empty, the modify is i
        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i
        for i in range(n):
            for j in range(m):
                if word1[i]==word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
        return dp[n][m]