class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # both are wrong, using single BFS will solve 
        # take the rotten as layer one
        # then in place going through them, the max layer is the ans
        # or if there's fresh orange left, ans -1
        # time:O(N*M) the size of the grid
        # space:O(M*N) or O(1) is we use the record in place
        org = []
        M = len(grid)
        N = len(grid[0])
        allOrgCnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    allOrgCnt += 1
                    org.append((i,j))
                if grid[i][j] == 1:
                    allOrgCnt += 1
        
        # coner case if no orange
        if allOrgCnt==0:
            return 0
        # using grid[i][j] = 3 as seen
        level = 0
        rotOrgCnt = 0
        while org:
            levelCnt = len(org)
            rotOrgCnt += levelCnt
            level+=1
            for i in range(levelCnt):
                rot = org.pop(0)
                x = rot[0]
                y = rot[1]
                if x-1>=0 and grid[x-1][y]==1:
                    org.append((x-1, y))
                    grid[x-1][y] = 3
                if x+1<M and grid[x+1][y]==1:
                    org.append((x+1, y))
                    grid[x+1][y] = 3
                if y-1>=0 and grid[x][y-1]==1:
                    org.append((x, y-1))
                    grid[x][y-1] = 3
                if y+1<N and grid[x][y+1]==1:
                    org.append((x, y+1))
                    grid[x][y+1] = 3
        return level-1 if rotOrgCnt == allOrgCnt else -1


        # brute:record the new rotten orange and each min sperete it out
        # if there's an fresh orange with no other orange around, then it's -1
        # time: O(N*M) M is the min
        # space: O(1) we could reuse the same grid
        # take the rotten as start, tree traverse the min dist to other fresh ones
        # record the fresh one as min dist to rotten
        # time:O(N*M) M is the num of rotten orange
        # space:O(1)
        