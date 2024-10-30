class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # record the word and it's idxs
        self.word2Idx = {}
        for idx in range(len(wordsDict)):
            w = wordsDict[idx]
            if w not in self.word2Idx.keys():
                self.word2Idx[w] = []
            self.word2Idx[w].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        # directly use the 2 idx array, for getting the distance by chaning the smaller index
        # of each word list, time:O(N+M)
        idx1 = 0
        idx2 = 0
        ret = abs(self.word2Idx[word1][0]-self.word2Idx[word2][0])
        while idx1<len(self.word2Idx[word1]) and idx2<len(self.word2Idx[word2]):
            nowDist = abs(self.word2Idx[word1][idx1]-self.word2Idx[word2][idx2])
            ret = min(ret, nowDist)
            
            if self.word2Idx[word1][idx1]<self.word2Idx[word2][idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return ret


        # use the shorter one to go through it's checking from the other array
        # time: O(N*logM)
        # shortW = word1
        # longW = word2
        # if len(self.word2Idx[word1])>len(self.word2Idx[word2]):
        #     shortW = word2
        #     longW = word1
        # # print(shortW, longW)
        # # print(self.word2Idx[shortW])
        # # print(self.word2Idx[longW])

        # ret = abs(self.word2Idx[word1][0]-self.word2Idx[word2][0])
        # for i in range(len(self.word2Idx[shortW])):
        #     checkIdx = self.word2Idx[shortW][i]
        #     lIdx = bisect.bisect_left(self.word2Idx[longW], checkIdx)
        #     if lIdx >= len(self.word2Idx[longW]):
        #         lIdx = len(self.word2Idx[longW])-1
        #     frontDist = abs(checkIdx - self.word2Idx[longW][lIdx])
        #     ret = min(ret, frontDist)
        #     # print(checkIdx, lIdx)
        #     lIdx -= 1
        #     if lIdx >= 0:
        #         frontDist = abs(checkIdx - self.word2Idx[longW][lIdx])
        #         ret = min(ret, frontDist)
        # return ret



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)