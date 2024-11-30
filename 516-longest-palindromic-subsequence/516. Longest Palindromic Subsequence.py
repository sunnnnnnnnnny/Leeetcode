class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp take or not take with prefix
        # time:O(N^2)
        vis = {}
        ret = 0
        n = len(s)
        def lps(l, r):
            nonlocal s, n, vis
            if l>r:
                return 0
            if (l,r) in vis:
                return vis[(l,r)]
            if l == r:
                return 1
            now = 0
            # print(l,r)
            if s[l] == s[r]:
                now = lps(l+1, r-1)+2
            else:
                now = max(lps(l, r-1), lps(l+1, r))
            vis[(l,r)] = now
            return now
        ret = lps(0,n-1)
        return ret
            
