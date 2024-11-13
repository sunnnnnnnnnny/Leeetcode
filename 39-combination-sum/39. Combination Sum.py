class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking with sort the num from increasing
        # try every num and get the target
        # time:O(N^(T/M+1)) space:O(T/N)
        candidates.sort()
        n = len(candidates)
        memo = {}
        ret = []
        def bk(nowLeft, nowIdx, nowRet):
            nonlocal memo, ret, candidates, n
            if nowLeft == 0:
                ret.append(list(nowRet))
                return 
            # if nowLeft in memo:
            #     return memo[nowLeft]
            for i in range(nowIdx, n):
                if candidates[i]>nowLeft:
                    break
                nowRet.append(candidates[i])
                bk(nowLeft-candidates[i], i, nowRet)
                nowRet.pop()
            return
        bk(target,0, [])
        return ret