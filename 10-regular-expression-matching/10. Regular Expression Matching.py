class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # match the characters then skip the 
        # bk with going forward with , time:O(N*M)
        sN = len(s)
        pN = len(p)
        memo = {}
        def bk(sIdx, pIdx):
            nonlocal sN, pN, s,p, memo
            if (sIdx, pIdx) in memo:
                return memo[(sIdx, pIdx)]
            ret = False
            if pIdx ==pN:
                ret = sIdx == sN
            else:
                # p[pIdx] should either be s[sIdx] or . for a match
                firstMatch = sIdx<sN and p[pIdx] in {s[sIdx], "."}
                # if the pattern is char* or .* we should deal them together
                if pIdx+1<pN and p[pIdx+1]=="*":
                    # skip the * or use it for further match
                    ret = bk(sIdx, pIdx+2) or firstMatch and bk(sIdx+1, pIdx)
                else:
                    ret = firstMatch and bk(sIdx+1, pIdx+1)
            memo[(sIdx, pIdx)] = ret
            return ret
        return bk(0,0)