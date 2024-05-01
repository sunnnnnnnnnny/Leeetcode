class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # get all the start time and end time
        # use binary search to get the insertion where the location of newInterval
        if len(newInterval) != 2:
            return intervals
        if len(intervals) == 0:
            return [newInterval]
        insertStart = newInterval[0]
        insertEnd = newInterval[1]
        ret = []
        idx = 0
        n = len(intervals)
        # add the interval not overlap with new one
        while idx < n and intervals[idx][1]<insertStart:
            ret.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0]<=insertEnd:
            insertStart = min(insertStart, intervals[idx][0])
            insertEnd = max(insertEnd, intervals[idx][1])
            idx += 1
        ret.append([insertStart, insertEnd])

        while idx < n:
            ret.append(intervals[idx])
            idx += 1
        return ret
        
