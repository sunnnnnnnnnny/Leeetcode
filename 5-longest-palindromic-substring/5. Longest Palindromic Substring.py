class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check by the middle for both odd and even ones
        # for odd is idx and even is idx, idx+1
        # time: O(N^2) as each try may take up going through N items
        # Space:O(1)
        def expandPar(l, r, rMax):
            while l>=0 and r<rMax:
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            sLen = max(r-l-1, 0)
            return sLen, l, r
        maxR = len(s)
        maxLen = 0
        ret = ""
        for idx in range(maxR):
            oddLen, rl, rr = expandPar(idx-1, idx+1, maxR)
            if oddLen>maxLen:
                ret = s[rl+1: rr]
            maxLen = max(maxLen, oddLen)
            evenLen, el, er = expandPar(idx, idx+1, maxR)
            if evenLen>maxLen:
                ret = s[el+1: er]
            maxLen = max(maxLen, evenLen)
        return ret

        