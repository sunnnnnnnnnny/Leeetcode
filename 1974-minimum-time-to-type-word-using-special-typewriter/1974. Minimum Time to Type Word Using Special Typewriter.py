class Solution:
    def minTimeToType(self, word: str) -> int:
        # get the min dist from current to next, with the start of a
        # time:O(N) space:O(1)
        curChar = 'a'
        def minDist(cur, want):
            clockWise = abs(ord(want)-ord(cur))
            countClock = 26-clockWise
            return min(clockWise, countClock)
        ret = len(word)
        for i in range(len(word)):
            ret += minDist(curChar, word[i])
            curChar = word[i]
        return ret
