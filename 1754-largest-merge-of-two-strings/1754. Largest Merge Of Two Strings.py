class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # greedly pick the larger char in both words, then we can get the latest lexicorgraphically one
        # time:O(N+M) space:O(N+M) if consider the result
        idx1, idx2 = 0, 0
        prev1, prev2 = 0,0
        n = len(word1)
        m = len(word2)
        ret = []
        # using greedy, while we can directly compare the words
        # and pick the start of that word head
        while idx1<n and idx2<m:
            if word1[idx1:]>word2[idx2:]:
                ret.append(word1[idx1])
                idx1+=1
            else:
                ret.append(word2[idx2])
                idx2+=1
        if idx1<n:
            ret.append(word1[idx1:])
        if idx2<m:
            ret.append(word2[idx2:])
        return "".join(ret)