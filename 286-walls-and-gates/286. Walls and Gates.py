class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # do bfs starting from each door and until no empty room can be reached
        # time: O(m*n) - the queue size may at most be O(m*n) = space
        startPos = []
        M = len(rooms)
        N = len(rooms[0])
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    startPos.append([i,j])
        levelCnt = 0
        # print(startPos)
        while len(startPos)>0:
            levelSize = len(startPos)
            for _ in range(levelSize):
                nowI, nowJ = startPos.pop(0)
                # visited
                if rooms[nowI][nowJ]>0 and rooms[nowI][nowJ]<2147483647:
                    continue
                rooms[nowI][nowJ] = levelCnt
                # 4 directions
                if nowI-1>=0 and rooms[nowI-1][nowJ]==2147483647:
                    startPos.append([nowI-1,nowJ])
                if nowI+1<M and rooms[nowI+1][nowJ]==2147483647:
                    startPos.append([nowI+1,nowJ])
                if nowJ-1>=0 and rooms[nowI][nowJ-1]==2147483647:
                    startPos.append([nowI,nowJ-1])
                if nowJ+1<N and rooms[nowI][nowJ+1]==2147483647:
                    startPos.append([nowI,nowJ+1])
            levelCnt+=1
        return