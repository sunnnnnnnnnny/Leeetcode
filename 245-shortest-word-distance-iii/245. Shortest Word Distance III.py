class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # get the idx of each words, then iterative the distance
        # time:O(N) space:O(1)
        w1Idx = -1
        w2Idx = -1
        ret = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                if word1 == word2:
                    prev = w1Idx
                    w1Idx = i
                    if prev > -1:
                        nowDist = w1Idx-prev
                        ret = min(ret, nowDist)

                else:
                    w1Idx = i
                    if w2Idx > -1:
                        nowDist = w1Idx-w2Idx
                        ret = min(ret, nowDist)
            elif wordsDict[i] == word2:
                w2Idx = i
                if w1Idx > -1:
                    nowDist = w2Idx-w1Idx
                    ret = min(ret, nowDist)
        return ret