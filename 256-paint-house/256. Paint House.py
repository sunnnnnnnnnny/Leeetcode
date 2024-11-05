class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp? dp[i] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2])+cost[i][0~2] which is allowed
        # time:O(3N) space:O(3N)
        n = len(costs)
        dp = [[-1 for _ in range(3)] for _ in range(n) ] 
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1,n):
            for j in range(3):
                prevMin = sum(dp[i-1])
                for x in range(3):
                    if x!=j:
                        prevMin = min(prevMin, dp[i-1][x])
                dp[i][j] = costs[i][j]+prevMin
        print(dp)
        return min(dp[n-1])