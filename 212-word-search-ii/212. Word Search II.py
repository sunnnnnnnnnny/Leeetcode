class TrieNode:
    def __init__(self, char, isWord):
        self.char = char
        self.child = defaultdict()
        self.isWord = isWord
        self.word = ""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # dfs for each word, time:O(N words * X*Y)
        # making the words as Trie then do backtracking on the board
        # time:O(M(4*3^L-1)) where L is the max len of word, M is cell count
        # the board having 4 direction but after dfs, it should left with only 3
        # thus the length of each cell as start will mostly go beyond 3^L-1
        # space:O(N) N is the total number of letters in the dictionary
        trieHead = TrieNode("", False)
        for word in words:
            prev = trieHead
            for i, c in enumerate(word):
                if c not in prev.child:
                    now = TrieNode(c, False)
                    prev.child[c] = now
                prev = prev.child[c]
                if i == len(word)-1:
                    prev.isWord = True
                    prev.word = word
        n = len(board)
        m = len(board[0])
        ret = []
        def dfs(nowI, nowJ, trieN):
            nonlocal ret, board, n, m
            if trieN.isWord:
                ret.append(trieN.word)
                trieN.isWord = False
            for i, j in [[1,0], [-1,0], [0,1], [0,-1]]:
                newI = nowI+i
                newJ = nowJ+j
                if newI<0 or newI>=n or newJ<0 or newJ>=m:
                    continue
                if board[newI][newJ] in trieN.child:
                    newChar = board[newI][newJ]
                    board[newI][newJ] = '#'
                    dfs(newI, newJ, trieN.child[newChar])
                    board[newI][newJ] = newChar
        for i in range(n):
            for j in range(m):
                if board[i][j] in trieHead.child:
                    newChar = board[i][j]
                    board[i][j] = '#'
                    dfs(i,j, trieHead.child[newChar])
                    board[i][j] = newChar
        return ret