class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # by going through both array we can get the procudt
        # record the num 2 freq direct and convert back to array
        # two pointers
        # time: O(N) space:O(N) for result
        oIdx = tIdx = 0
        oinidx = tinidx = 0
        ret = []
        while oIdx<len(encoded1) and tIdx<len(encoded2):
            oNum = encoded1[oIdx][0]
            oFreq = encoded1[oIdx][1]
            tNum = encoded2[tIdx][0]
            tFreq = encoded2[tIdx][1]

            prodSetCnt = min(oFreq, tFreq)
            prod = oNum*tNum
            if len(ret)>0 and prod==ret[-1][0]:
                ret[-1][1] += prodSetCnt
            else:
                ret.append([prod, prodSetCnt])
            encoded1[oIdx][1] -= prodSetCnt
            encoded2[tIdx][1] -= prodSetCnt
            if encoded1[oIdx][1] == 0:
                oIdx += 1
            if encoded2[tIdx][1] == 0:
                tIdx += 1
        
        return ret

