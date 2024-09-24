class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time, with traversing the whole intervals
        # where merge the overlap
        # time:O(nlogn+n) space:O(n) for sorting
        intervals.sort(key = lambda x:x[0])
        ret = [intervals[0]]
        for i in range(1,len(intervals)):
            prevS, prevE = ret[-1]
            nowS, nowE = intervals[i]
            # having overlap
            if nowS>=prevS and nowS<=prevE:
                ret[-1][1] = max(ret[-1][1], nowE)
            else:
                ret.append(intervals[i])
        return ret