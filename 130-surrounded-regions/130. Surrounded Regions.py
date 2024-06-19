class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs the whole area of O, if it meets the boarder, 
        # then it's not a surronded area.
        # time:O(2*N*M) space:O(1)=>wrong as there's the stack thus O(N*M)
        M = len(board)
        N = len(board[0])
        def dfsToE(x, y):
            if x-1>=0 and board[x-1][y] == 'O':
                board[x-1][y] = 'E'
                dfsToE(x-1, y)
            if x+1<M and board[x+1][y] == 'O':
                board[x+1][y] = 'E'
                dfsToE(x+1, y)
            if y-1>=0 and board[x][y-1] == 'O':
                board[x][y-1] = 'E'
                dfsToE(x, y-1)
            if y+1<N and board[x][y+1] == 'O':
                board[x][y+1] = 'E'
                dfsToE(x, y+1)
            return
        # use the boarder O cell as to mark the cell not able to be surrounded
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    if i==0 or i==M-1 or j==0 or j==N-1:
                        board[i][j] = 'E'
                        dfsToE(i, j)
        # use E as the temp to mark escaped O so we don't traverse again,
        # then need to set it back
        # print(board)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return 


        