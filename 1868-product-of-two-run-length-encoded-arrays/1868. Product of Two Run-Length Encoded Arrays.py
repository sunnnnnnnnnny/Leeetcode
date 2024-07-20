class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # by going through both array we can get the procudt
        # record the num 2 freq direct and convert back to array
        oIdx = tIdx = 0
        oinidx = tinidx = 0
        ret = []
        while oIdx<len(encoded1) and tIdx<len(encoded2):
            oNum = encoded1[oIdx][0]
            oFreq = encoded1[oIdx][1]
            tNum = encoded2[tIdx][0]
            tFreq = encoded2[tIdx][1]
            while oinidx<oFreq and tinidx<tFreq:
                oLeft = oFreq-oinidx
                tLeft = tFreq-tinidx
                prodSetCnt = min(oLeft, tLeft)
                prod = oNum*tNum
                if len(ret)>0 and prod==ret[-1][0]:
                    ret[-1][1] += prodSetCnt
                else:
                    ret.append([prod, prodSetCnt])
                oinidx += prodSetCnt
                tinidx += prodSetCnt
            if oinidx>=oFreq:
                oinidx = 0
                oIdx += 1
            if tinidx>=tFreq:
                tinidx = 0
                tIdx += 1
        
        return ret

