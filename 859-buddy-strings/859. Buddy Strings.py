class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # check the frequency with the cnts, and at most 2 place could be differentt
        # time:O(N) space:O(N)
        if len(s)!=len(goal):
            return False
        sCnt = collections.Counter(s)
        gCnt = collections.Counter(goal)
        if len(sCnt.keys())!=len(gCnt.keys()):
            return False
        freqDouble = False
        for i,freq in sCnt.items():
            if i not in gCnt.keys():
                return False
            if gCnt[i] != freq:
                return False
            if freq>=2:
                freqDouble = True
        diffCnt = 0
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diffCnt+=1
                if diffCnt>2:
                    return False
        
        return True if diffCnt == 2 else freqDouble