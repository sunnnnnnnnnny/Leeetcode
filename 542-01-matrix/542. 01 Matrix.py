class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # every 0 makes bfs traversal to overwrite the shorest dist to other pos
        # time:O(N*M) space:O(N*M)
        n = len(mat)
        m = len(mat[0])
        locQ = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    locQ.append((i,j))
        level = 0
        dist = [[-1 for i in range(m)] for j in range(n)]
        while locQ:
            levelSize = len(locQ)
            for i in range(levelSize):
                nowi, nowj = locQ.pop(0)
                if dist[nowi][nowj] != -1:
                    continue
                dist[nowi][nowj] = level
                if nowi-1>=0 and mat[nowi-1][nowj]==1 and dist[nowi-1][nowj]==-1:
                    locQ.append((nowi-1,nowj))
                if nowi+1<n and mat[nowi+1][nowj]==1 and dist[nowi+1][nowj]==-1:
                    locQ.append((nowi+1,nowj))
                if nowj-1>=0 and mat[nowi][nowj-1]==1 and dist[nowi][nowj-1]==-1:
                    locQ.append((nowi,nowj-1))
                if nowj+1<m and mat[nowi][nowj+1]==1 and dist[nowi][nowj+1]==-1:
                    locQ.append((nowi,nowj+1))
            level += 1
        return dist