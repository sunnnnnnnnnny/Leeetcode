class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window, making the window size as len(p)
        # if the count is of sub_s is same as p, then we find one anagram
        # the time if not consider the checking of sCnt == pCnt
        # time:O(len(s))
        # time:O(len(s)*len(p)) because checking the count of p, for each sub_s
        # space:O(26)=O(1)
        if len(s)<len(p):
            return []
        pCount = [0 for _ in range(26)]
        sCount = [0 for _ in range(26)]
        p.lower()
        for i in range(len(p)):
            nowI = int(ord(p[i])-ord('a'))
            pCount[nowI]+=1
            nowsI = int(ord(s[i])-ord('a'))
            sCount[nowsI]+=1
        # def sCntEqpCnt(sCount, pCount):
        #     for i in range(len(sCount)):
        #         if sCount[i]!=pCount[i]:
        #             return False
        #     return True
        ret = []
        if sCount == pCount:
            ret.append(0)
        preIdx = 0
        for i in range(len(p), len(s)):
            prevI = int(ord(s[preIdx])-ord('a'))
            sCount[prevI]-=1
            preIdx+=1
            nowsI = int(ord(s[i])-ord('a'))
            sCount[nowsI]+=1
            # if sCntEqpCnt(sCount, pCount):
            #     ret.append(preIdx)
            if sCount == pCount:
                ret.append(preIdx)
        return ret