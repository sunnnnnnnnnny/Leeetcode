class Solution:
    def countOrders(self, n: int) -> int:
        # the only constriant is Pi<Di, seem like a math
        # use the permutation pattern, for each pattern the possibility would be n*N-1*...*1 equal to n!
        ret = 0
        memo = [[-1 for i in range(n+1)]for j in range(n+1)]
        def bkWays(openCnt, closeCnt):
            nonlocal ret, memo
            if openCnt<0 or closeCnt<0:
                return 0
            if memo[openCnt][closeCnt] != -1:
                return memo[openCnt][closeCnt]
            waysToPick = openCnt*bkWays(openCnt-1, closeCnt)
            waysToDelivery = (closeCnt-openCnt)*bkWays(openCnt, closeCnt-1)
            memo[openCnt][closeCnt] = (waysToPick+waysToDelivery) % 1000000007
            return memo[openCnt][closeCnt]
        memo[0][0] = 1
        bkWays(n, n)
        return memo[n][n]

        # def backtrack(openArr, closeArr):
        #     nonlocal ret,n
        #     if len(openArr)==n and len(closeArr)==0:
        #         ret+=1
        #         ret = ret % 1000000007
        #         return
        #     for op in range(n):
        #         if op not in openArr:
        #             openArr.add(op)
        #             closeArr.add(op)
        #             backtrack(openArr, closeArr)
        #             openArr.remove(op)
        #             closeArr.remove(op)
        #     for en in range(n):
        #         if en in closeArr:
        #             closeArr.remove(en)
        #             backtrack(openArr, closeArr)
        #             closeArr.add(en)
        # backtrack(set(), set())
        # return ret
                
