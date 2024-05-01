class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by ending interval
        # greedy picking the earlier ending one interval one
        # the same question of maximum none overlapping interval
        intervals.sort(key=lambda x:x[1])
        nowEnd = intervals[0][0]-1
        ret = 0
        for interval in intervals:
            if nowEnd<=interval[0]:
                nowEnd = interval[1]
                ret += 1
            else:
                nowEnd = min(interval[1], nowEnd)
        left = len(intervals) - ret
        return left

        