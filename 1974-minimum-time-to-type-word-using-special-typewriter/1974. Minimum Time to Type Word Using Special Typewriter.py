class Solution:
    def minTimeToType(self, word: str) -> int:
        # get the min dist from current to next, with the start of a
        # time:O(N) space:O(1)
        def minDist(cur, want):
            clockWise = abs(ord(want)-ord(cur))
            countClock = 26-clockWise
            return min(clockWise, countClock)
        ret = len(word)+minDist('a', word[0])
        for i in range(1, len(word)):
            ret += minDist(word[i-1], word[i])
        return ret
