class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # by going through the wordsDict, keep updating the idx
        # and get the shortest dist 
        # time:O(N) space:O(1)
        idx1 = -1
        idx2 = -1
        ret = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                if idx2 != -1:
                    dist = abs(i-idx2)
                    ret = min(ret, dist)
                idx1 = i
            elif wordsDict[i] == word2:
                if idx1 != -1:
                    dist = abs(i-idx1)
                    ret = min(ret, dist)
                idx2 = i
        return ret

