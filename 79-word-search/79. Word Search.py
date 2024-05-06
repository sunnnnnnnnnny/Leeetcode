class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # traverse the board to get the head
        # use dfs to find possible word
        # record the same letter used by changing the char tempuraily
        # Time: O(N*3^L) L is the length of word =, N is the size of board
        # Space: O(L) the recursion call is at max depth of word length 
        nextDir = [[1,0], [-1,0], [0,1], [0,-1]]
        def searchSuffix(x, y, maxX, maxY, suffix):
            if suffix == "":
                return True
            if x<0 or x>=maxX or y<0 or y>=maxY:
                return False
            if board[x][y] == '#':
                return False
            oriChar = board[x][y]
            if board[x][y] == suffix[0]:
                board[x][y] = '#'
                for dir in nextDir:
                    nextX = x+dir[0]
                    nextY = y+dir[1]
                    if searchSuffix(nextX, nextY, maxX, maxY, suffix[1:]):
                        return True
                board[x][y] = oriChar
                # in case no where to go we still need to check if this is end
            return False
        maxX = len(board)
        maxY = len(board[0])
        # print('maxX maxY', maxX, maxY)
        for i in range(maxX):
            for j in range(maxY):
                if searchSuffix(i, j, maxX, maxY, word):
                    return True
        return False
        

                
                
            
        
        