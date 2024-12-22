class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # precalculate the counts and using the range to directly deducute
        # time:O(N+M) n is words, m is query
        # space:O(N)
        vowelCnt = 0
        def isSEvow(w):
            if w[0] in set('aeiou') and w[-1] in set('aeiou'):
                return True
            return False
        n = len(words)
        wCnt = [0]*(n+1)
        for i in range(n):
            if isSEvow(words[i]):
                vowelCnt+=1
            wCnt[i+1] = vowelCnt
        ret = []
        for q1, q2 in queries:
            nowRet = wCnt[q2+1]-wCnt[q1]
            ret.append(nowRet)
        return ret