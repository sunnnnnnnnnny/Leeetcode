class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # map the character of s and t to which they have the same char
        # start traversing from left, then if the mapping is n-1 then true
        sN = len(s)
        tN = len(t)
        if sN>tN:
            return self.isOneEditDistance(t, s)
        if tN-sN>1 or (s==t):
            return False
        sIdx = 0
        tIdx = 0
        matchCnt = 0
        
        while sIdx<sN and tIdx<tN:
            if s[sIdx] == t[tIdx]:
                sIdx += 1
                tIdx += 1
                matchCnt += 1
            else:
                break
        if sN==tN:
            sIdx += 1
            tIdx += 1
        else:
            tIdx +=1
        while sIdx<sN and tIdx<tN:
            if s[sIdx] == t[tIdx]:
                sIdx += 1
                tIdx += 1
                matchCnt += 1
            else:
                break
        # print(matchCnt)
        return True if matchCnt>=tN-1 else False
