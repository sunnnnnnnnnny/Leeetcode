class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # check if overlapped intervals
        # sort by start time, then traverse all the interval
        # by keep tracking of current end time
        # Time: O(NlogN+N) sort + travese
        # Space: O(N) sorting
        if len(intervals) == 0:
            return True
        intervals.sort(key= lambda x:x[0])
        nowEnd = intervals[0][0]-1
        for start, end in intervals:
            if start<nowEnd:
                return False
            nowEnd = end
        return True
        