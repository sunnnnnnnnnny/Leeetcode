class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # dp get if this coin will be head or tail
        # the sum of all those probability is the result
        # time: O(target*N) space: O(target*N)
        # dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])
        ret = 0
        totalCoin = len(prob)
        memo = {}
        # memo[index][target] records the prob of using index before with target
        
        def bt(nowI, leftTargetCnt):
            nonlocal totalCoin, ret
            if leftTargetCnt<0:
                return 0
            if nowI == totalCoin:
                # only when left Target is reached, this probability is valid
                if leftTargetCnt == 0:
                    return 1
                else:
                    return 0
            if (nowI, leftTargetCnt) in memo:
                return memo[nowI, leftTargetCnt]

                # now is head 
                # 1-now is tail
            memo[nowI,leftTargetCnt] = \
                bt(nowI+1, leftTargetCnt-1)*prob[nowI]+\
                bt(nowI+1, leftTargetCnt)*(1-prob[nowI])
            return memo[nowI,leftTargetCnt]
        
        return bt(0, target)

        