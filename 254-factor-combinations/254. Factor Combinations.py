class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # get all the smallest factor, then dp creating it
        ret = []
        def getSmallestFactor(n, cur):
            nonlocal ret
            start  = cur[-1] if len(cur)>0 else 2
            if n<start:
                return
            
            oneRet = []
            if len(cur)>0:
                oneRet.append(n)
                oneRet.extend(cur)
                ret.append(oneRet)
            # print(n, start, cur)
            for i in range(start,n-1):
                if n%i == 0:
                    if n//i < start:
                        break
                    cur.append(i)
                    getSmallestFactor(n//i, cur)
                    cur.pop()
                    # return
            return
        getSmallestFactor(n, [])
        # print(ret)
        return ret


