class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # sliding window, time:O(N) space:O(N)
        n = len(code)
        if k == 0:
            return [0]*n
        placeI = n-1
        if k<0:
            k = -k
            placeI = k
        ret = [0]*n
        nowSum = 0
        for i in range(k):
            nowSum += code[i]
        def cirIdx(nowI):
            nonlocal n
            nowI += 1
            if nowI == n:
                nowI = 0
            return nowI
        idxS = 0
        idxE = k
        for i in range(n):
            ret[placeI] = nowSum
            nowSum -= code[idxS]
            nowSum += code[idxE]
            idxS  = cirIdx(idxS)
            idxE = cirIdx(idxE)
            placeI = cirIdx(placeI)
        return ret

