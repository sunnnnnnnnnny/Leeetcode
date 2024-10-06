class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # get the count of difference character
        # the min num is the sum of difference freq count of each char
        # time:O(N+26) = O(N) space:O(26) = O(1)
        if len(s) != len(t):
            return -1
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)
        # print(sCount)
        # print(tCount)
        ret = 0
        for k,v in sCount.items():
            tCnt = 0
            if k in tCount.keys():
                tCnt = tCount[k]
            if v>=tCnt:
                ret += (v-tCnt)
        return ret