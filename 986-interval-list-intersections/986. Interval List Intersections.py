class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # one pair can only be intersect to another pair in the list due to disjoint feature
        # go through both first and scond to find the intersec
        # time:O(N) space:O(1) if not considering the result
        fIdx = sIdx = 0
        ret = []
        while fIdx<len(firstList) and sIdx<len(secondList):
            fStart = firstList[fIdx][0]
            fEnd = firstList[fIdx][1]
            sStart = secondList[sIdx][0]
            sEnd = secondList[sIdx][1]
            if fEnd<sStart:
                fIdx+=1
            elif sEnd<fStart:
                sIdx+=1
            else:
                # find intersect
                iStart = max(fStart, sStart)
                iEnd = min(fEnd, sEnd)
                ret.append([iStart, iEnd])
                if fEnd<sEnd:
                    fIdx+=1
                else:
                    sIdx+=1
        return ret
