class Solution:
    def countSubstrings(self, s: str) -> int:
        # go through each idx as the middle and the even ones
        # count each possible palindromic
        # time: O(N^2)
        # Space: O(1)
        def countPalidronmic(l, r, rMax):
            cnt = 0
            while l>=0 and r<rMax:
                if s[l] != s[r]:
                    break
                else:
                    cnt+=1
                    l-=1
                    r+=1
            return cnt
        totalCnt = 0
        rMax = len(s)
        for idx in range(rMax):
            oddCnt = countPalidronmic(idx-1, idx+1, rMax)
            evenCnt = countPalidronmic(idx, idx+1, rMax)
            totalCnt += oddCnt
            totalCnt += evenCnt
            # add it's self
            totalCnt+=1
        return totalCnt

        