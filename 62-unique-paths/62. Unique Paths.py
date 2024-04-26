class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # as only move is down or right
        # dp[i][j] = dp[i-1][j]+dp[i][j-1]
        def dp(self, x:int, y:int) -> int:
            if x==0 and y==0:
                return 1
            if x<0 or y<0:
                return 0
            key = str(x)+'_'+str(y)
            if key in self.memo:
                return self.memo[key]
            uniWays = dp(self, x-1, y)+dp(self, x, y-1)
            self.memo[key] = uniWays
            return uniWays
        self.memo = {}
        # the grid size is larger than the index, thus need to minus 1
        return dp(self, m-1, n-1)