class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # do dfs to use the maze as dag
        # time:O(n*M*(n+m))
        # need to go to the very end to get the DAG 
        # space:O(N*M)
        n = len(maze)
        m = len(maze[0])
        startX, startY = start
        destX, destY = destination
        dirct = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        ret = False
        def dfs(x,y):
            nonlocal destX, destY, maze, ret, visited
            if x == destX and y == destY:
                ret = True
                return
            if (x,y) in visited:
                return 
            # mark as visited
            visited.add((x,y))
            for d in dirct:
                dx, dy = d
                while x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<m and maze[x+dx][y+dy]==0:
                    dx+= d[0]
                    dy+=d[1]
                dx-=d[0]
                dy-=d[1]
                dfs(x+dx,y+dy)
        dfs(startX, startY)
        return ret

            