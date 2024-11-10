class Solution:
    def houseOfCards(self, n: int) -> int:
        # formular of a valid row is 2+3*x where x>=1
        # dp key as card left and bottom size
        memo = {}
        ret = 0
        def bk(leftCard, bottomSize, level):
            nonlocal ret, memo
            # print(leftCard, bottomSize)
            if leftCard == 0:
                return 1
            if (leftCard, bottomSize) in memo:
                return memo[(leftCard, bottomSize)]
            if leftCard <2:
                memo[(leftCard, bottomSize)] = 0
                return 0
            btnSize = 0
            nowRet = 0
            for i in range(2, leftCard+1, 3):
                if bottomSize>=0 and btnSize+1>bottomSize:
                    break
                nowRet += bk(leftCard-i, btnSize, level+1)
                btnSize += 1
            
            memo[(leftCard, bottomSize)] = nowRet
            return nowRet
        ret = bk(n, -1,0)
        return ret