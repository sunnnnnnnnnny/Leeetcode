class Solution:
    def countBits(self, n: int) -> List[int]:
        # Should be the sum of i from clostest 2 mulriples
        ret = []
        pre = 0
        start = 1
        for i in range(0, n+1, 1):
            iCnt = 0
            if i<start:
                if i==pre:
                    if pre>0:
                        iCnt = 1
                else:
                    iCnt = ret[pre]
                    iLeft = i-pre
                    iCnt += ret[iLeft]
            else:
                pre = start
                start *= 2
                iCnt = 1
            ret.append(iCnt)
        return ret

            
