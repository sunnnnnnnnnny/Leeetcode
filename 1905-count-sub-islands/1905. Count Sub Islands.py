class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # traverse the whole grid2 for each island and check the land exist in grid1
        # thus through dfs or bfs taking 
        # time:O(m*n) space:O(1) if we modify visited in place
        def dfs(nowX, nowY, m, n, isSub):
            nonlocal grid1, grid2
            # print("dfs head:", nowX, nowY)
            if nowX<0 or nowX>=m or nowY<0 or nowY>=n or grid2[nowX][nowY] != 1:
                return isSub
            # if grid2[nowX][nowY] is not 1:
            #     return isSub
            isSub = isSub and grid1[nowX][nowY]==1
            grid2[nowX][nowY] = 2
            isSub1 = dfs(nowX+1, nowY, m, n, isSub)
            isSub2 = dfs(nowX-1, nowY, m, n, isSub)
            isSub3 = dfs(nowX, nowY+1, m, n, isSub)
            isSub4 = dfs(nowX, nowY-1, m, n, isSub)
            return isSub and isSub1 and isSub2 and isSub3 and isSub4
        m = len(grid1)
        n = len(grid1[0])
        print(m,n)
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    # print("Island start-------")
                    # print(i, j)
                    # print("-------")
                    currentIsSub = dfs(i, j, m, n, True)
                    if currentIsSub:
                        ret += 1
                    # print(grid2)
        return ret
            