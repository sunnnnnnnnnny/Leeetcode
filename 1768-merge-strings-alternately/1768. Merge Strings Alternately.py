class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # take the idx of both items, then go with it.
        # time:O(max(N,M)) space:O(N+M)
        idx1 = idx2 = 0
        n = len(word1)
        m = len(word2)
        ret = []
        while idx1< n and idx2<m:
            ret.append(word1[idx1])
            ret.append(word2[idx2])
            idx1+=1
            idx2+=1
        if idx1<n:
            ret.append(word1[idx1:])
        if idx2<m:
            ret.append(word2[idx2:])
        return "".join(ret)