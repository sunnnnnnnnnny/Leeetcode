class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs with memo? 
        # time:O(N*M) space:O(N*M)
        n = len(matrix)
        m = len(matrix[0])
        memo = [[-1 for _ in range(m)] for _ in range(n)]
        def dfs(nowx, nowy):
            nonlocal memo, matrix, n, m
            if memo[nowx][nowy]!= -1:
                return memo[nowx][nowy]
            nextLongDist = 0
            if nowx-1>=0 and matrix[nowx][nowy]<matrix[nowx-1][nowy]:
                nextDist = dfs(nowx-1, nowy)
                nextLongDist = max(nextLongDist, nextDist)
            if nowx+1<n and matrix[nowx][nowy]<matrix[nowx+1][nowy]:
                nextDist = dfs(nowx+1, nowy)
                nextLongDist = max(nextLongDist, nextDist)
            if nowy-1>=0 and matrix[nowx][nowy]<matrix[nowx][nowy-1]:
                nextDist = dfs(nowx, nowy-1)
                nextLongDist = max(nextLongDist, nextDist)
            if nowy+1<m and matrix[nowx][nowy]<matrix[nowx][nowy+1]:
                nextDist = dfs(nowx, nowy+1)
                nextLongDist = max(nextLongDist, nextDist)
            memo[nowx][nowy] = nextLongDist+1
            return memo[nowx][nowy]
        ret = 0
        for i in range(n):
            for j in range(m):
                ret = max(ret, dfs(i,j))
        return ret