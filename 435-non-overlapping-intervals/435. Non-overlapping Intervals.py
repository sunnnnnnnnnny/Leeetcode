class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by ending interval
        # greedy picking the earlier ending one interval one
        # the same question of maximum none overlapping interval
        # time: O(NlogN+N)=> O(nlogn) sort+traversal
        # space: O(N) b/c the sorting of Timesort in python
        intervals.sort(key=lambda x:x[1])
        # the first ending should be not overlapped with the first interval
        # could also use -inf
        # nowEnd = intervals[0][0]-1
        nowEnd = -inf
        ret = 0
        for interval in intervals:
            if nowEnd<=interval[0]:
                nowEnd = interval[1]
                ret += 1
            else:
                nowEnd = min(interval[1], nowEnd)
        left = len(intervals) - ret
        return left

        