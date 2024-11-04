class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort with the end then any non-overlapped is the good one
        # time:O(nlogn) space:O(1)
        intervals.sort(key = lambda x:x[1])
        prev = intervals[0][1]
        ret = 0
        for i in range(1, len(intervals)):
            if intervals[i][0]<prev:
                ret += 1
            else:
                prev = intervals[i][1]
        return ret