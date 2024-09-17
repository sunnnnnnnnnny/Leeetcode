class TicTacToe:
    #  initial the board with size n*n with 0 as indicating th eempty
    # with playerID we marked the spot as it's ID
    # when adding a move, we don't need to go through the whole board
    # b/c the only space that makes difference is the new spot, 
    # doing 3 direction checking for the added location
    # q: does it allows to add more move after one wins? what to expect for return
    # time:O(n*n) for creating board
    # move:O(N) space:O(N*N) for board
    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.Winner = 0
        self.NSize = n

    def move(self, row: int, col: int, player: int) -> int:
        n = self.NSize
        if self.Winner != 0:
            return self.Winner
        self.board[row][col] = player
        # check the 3 directions
        if row == col or row+col == n-1:
            # check diagonal
            diaCnt = 0
            dia2Cnt = 0
            for i in range(n):
                if self.board[i][i] == player:
                    diaCnt+=1
                if self.board[i][n-1-i] == player:
                    dia2Cnt+=1
            if diaCnt==n or dia2Cnt==n:
                self.Winner = player
                return self.Winner
        rowCnt = colCnt = 0
        for i in range(n):
            if self.board[row][i] == player:
                rowCnt+=1
            if self.board[i][col] == player:
                colCnt+=1
        if rowCnt==n or colCnt==n:
            self.Winner = player
        return self.Winner
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)