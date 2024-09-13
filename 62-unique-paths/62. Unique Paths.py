class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = from up dp[i-1][j]+ from left dp[i][j-1]
        # dp[i][j] will be the unique way for the robot to reach this location
        # time: O(N*M) space:O(N*M)
        # bottom-up with getting the direction from up to bottom and left to right
        dp = [[0 for i in range(n) ] for j in range(m)]
        # assume n&m>0 set up base condition
        # could modify to save space with only record the previous row-O(N)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
