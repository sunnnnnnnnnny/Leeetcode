class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # only consider the endtime, thus sort by earlier end time
        # greedy getting the non overlapping one, cnt how many overlapped
        # time: O(NlogN) space:O(N) because the sort
        # sorted(intervals, key= lambda x:(x[0],x[1]))
        intervals = sorted(intervals, key= lambda x:x[1])
        # print(intervals)
        lastTime = intervals[0]
        ret = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start<lastTime[1]:
                ret+=1
                continue
            lastTime = intervals[i]
        return ret