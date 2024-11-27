class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check if the char mapping is correct
        # time:O(N) space:O(N)
        pairS = {}
        pairT = {}
        if len(s)!=len(t):
            return False
        
        for a, b in zip(s,t):
            if a in pairS and pairS[a]!=b:
                return False
            if b in pairT and pairT[b]!=a:
                return False
            pairS[a] = b
            pairT[b] = a
        return True