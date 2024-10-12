class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dfs with the time of reaching (n-1, n-1) would be the max of elevation
        # time:O(4^N*m) space:O(N*m)
        # bfs+priority queue with only pop out the shortest time to reach 
        # time:O(n*M*log(n*M))
        n = len(grid)
        m = len(grid[0])
        ret = [[-1 for j in range(m)] for j in range(n)]

        bfsQueue = []
        heapq.heappush(bfsQueue, (grid[0][0],0,0))
        while bfsQueue:
            nowCost, nowI, nowJ = heapq.heappop(bfsQueue)
            if ret[nowI][nowJ]!= -1:
                continue
            ret[nowI][nowJ] = nowCost
            if nowI-1>=0 and ret[nowI-1][nowJ] == -1:
                heapq.heappush(bfsQueue, (max(nowCost, grid[nowI-1][nowJ]),nowI-1,nowJ))
            if nowI+1<n and ret[nowI+1][nowJ] == -1:
                heapq.heappush(bfsQueue, (max(nowCost, grid[nowI+1][nowJ]),nowI+1,nowJ))
            if nowJ-1>=0 and ret[nowI][nowJ-1] == -1:
                heapq.heappush(bfsQueue, (max(nowCost, grid[nowI][nowJ-1]),nowI,nowJ-1))
            if nowJ+1<m and ret[nowI][nowJ+1] == -1:
                heapq.heappush(bfsQueue, (max(nowCost, grid[nowI][nowJ+1]),nowI,nowJ+1))
        return ret[n-1][m-1]


        # def dfs(nowi, nowj, maxEle, visited):
        #     nonlocal n, m, grid, ret
        #     if ret[nowi][nowj] != -1 and ret[nowi][nowj]<maxEle:
        #         return 
        #     ret[nowi][nowj] = maxEle
        #     if nowi-1>=0 and (nowi-1, nowj) not in visited:
        #         visited.add((nowi-1, nowj))
        #         dfs(nowi-1, nowj, max(maxEle, grid[nowi-1][nowj]), visited)
        #         visited.remove((nowi-1, nowj))
        #     if nowi+1<n and (nowi+1, nowj) not in visited:
        #         visited.add((nowi+1, nowj))
        #         dfs(nowi+1, nowj, max(maxEle, grid[nowi+1][nowj]), visited)
        #         visited.remove((nowi+1, nowj))
        #     if nowj-1>=0 and (nowi, nowj-1) not in visited:
        #         visited.add((nowi, nowj-1))
        #         dfs(nowi, nowj-1, max(maxEle, grid[nowi][nowj-1]), visited)
        #         visited.remove((nowi, nowj-1))
        #     if nowj+1<m and (nowi, nowj+1) not in visited:
        #         visited.add((nowi, nowj+1))
        #         dfs(nowi, nowj+1, max(maxEle, grid[nowi][nowj+1]), visited)
        #         visited.remove((nowi, nowj+1))
        # visit = set()
        # dfs(0,0,grid[0][0], visit)
        # return ret[n-1][m-1]

