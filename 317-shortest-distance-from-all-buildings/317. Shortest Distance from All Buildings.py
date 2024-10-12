class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # time:O(N^2*M^2) space:O(N*m)
        targetCnt = 0
        friendLoc = []
        n =len(grid)
        m = len(grid[0])
        distCnt = [[0 for i in range(m)] for j in range(n)]
        def bfs(startI, startJ, nowIdx):
            nonlocal n, m, grid, distCnt
            bfsQueue = [(startI, startJ)]
            dist =0
            ret = -1
            while bfsQueue:
                levelCnt = len(bfsQueue)
                for i in range(levelCnt):
                    nowI, nowJ = bfsQueue.pop(0)
                    if grid[nowI][nowJ]<=0:
                        if grid[nowI][nowJ] < -nowIdx:
                            continue
                        grid[nowI][nowJ] -=1
                        distCnt[nowI][nowJ] += dist
                        ret = min(ret, distCnt[nowI][nowJ]) if ret>-1 else distCnt[nowI][nowJ]
                    if nowI-1>=0 and grid[nowI-1][nowJ]<=0 and grid[nowI-1][nowJ]== -nowIdx:
                        bfsQueue.append((nowI-1, nowJ))
                    if nowI+1<n and grid[nowI+1][nowJ]<=0 and grid[nowI+1][nowJ]== -nowIdx:
                        bfsQueue.append((nowI+1, nowJ))
                    if nowJ-1>=0 and grid[nowI][nowJ-1]<=0 and grid[nowI][nowJ-1]== -nowIdx:
                        bfsQueue.append((nowI, nowJ-1))
                    if nowJ+1<m and grid[nowI][nowJ+1]<=0 and grid[nowI][nowJ+1]== -nowIdx:
                        bfsQueue.append((nowI, nowJ+1))
                dist+=1
            # print(startI, startJ)
            # print(grid)
            # print(distCnt)
            return ret
        finalRet = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    finalRet = bfs(i, j, targetCnt)
                    targetCnt +=1
        # print(distCnt)
        return finalRet

        # dist = 0
        # ret = -1
        # while friendLoc:
        #     levelCnt = len(friendLoc)
        #     for i in range(levelCnt):
        #         nowi, nowj, friendIdx = friendLoc.pop(0)
        #         seenCnt[nowi][nowj][0]+=1
        #         seenCnt[nowi][nowj][1]+=dist
        #         if grid[nowi][nowj] == 0 and seenCnt[nowi][nowj][0] == targetCnt:
        #             # print(nowi, nowj, friendIdx, dist)
        #             # return seenCnt[nowi][nowj][1]+dist
        #             ret = min(ret, seenCnt[nowi][nowj][1]) if ret!=-1 else seenCnt[nowi][nowj][1]
        #         if nowi-1>=0 and grid[nowi-1][nowj]==0 and (nowi-1, nowj) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi-1, nowj))
        #             friendLoc.append((nowi-1, nowj, friendIdx))
        #         if nowi+1<n and grid[nowi+1][nowj]==0  and (nowi+1, nowj) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi+1, nowj))
        #             friendLoc.append((nowi+1, nowj, friendIdx))
        #         if nowj-1>=0 and grid[nowi][nowj-1]==0 and (nowi, nowj-1) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi, nowj-1))
        #             friendLoc.append((nowi, nowj-1, friendIdx))
        #         if nowj+1<m and grid[nowi][nowj+1]==0 and (nowi, nowj+1) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi, nowj+1))
        #             friendLoc.append((nowi, nowj+1, friendIdx))
        #     dist+=1
        # return ret